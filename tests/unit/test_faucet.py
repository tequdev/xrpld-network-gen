#!/usr/bin/env python
# coding: utf-8

from xrpld_netgen.faucet import generate_faucet_dockerfile, generate_faucet_server


def test_generated_faucet_server_persists_wallet_seed():
    server = generate_faucet_server()

    assert 'FAUCET_WALLET_PATH' in server
    assert 'readFileSync(FAUCET_WALLET_PATH, "utf8")' in server
    assert 'Wallet.fromSeed(stored.seed)' in server
    assert 'stored.address !== wallet.address' in server
    assert 'address: wallet.address, seed: wallet.seed' in server
    assert 'mode: 0o600' in server


def test_generated_faucet_server_only_funds_a_missing_account():
    server = generate_faucet_server()

    assert 'faucetAccountExists(client, faucetWallet)' in server
    assert 'console.log("Reusing funded faucet wallet")' in server


def test_generated_faucet_image_does_not_copy_wallet_data():
    dockerfile = generate_faucet_dockerfile()

    assert "COPY src ./src" in dockerfile
    assert "COPY . ." not in dockerfile
