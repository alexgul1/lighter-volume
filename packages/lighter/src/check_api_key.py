import asyncio
import lighter
import eth_account


async def get_account_index():
    # Ваш Ethereum адрес (кошелек, который вы используете на Lighter)
    ETH_ADDRESS = "0x222579322A3159c4C37581F01cbfEB81179C6D11"  # Ваш адрес кошелька

    BASE_URL = "https://testnet.zklighter.elliot.ai"

    configuration = lighter.Configuration(BASE_URL)
    api_client = lighter.ApiClient(configuration)
    account_api = lighter.AccountApi(api_client)

    try:
        # Получаем информацию об аккаунте по L1 адресу
        response = await account_api.accounts_by_l1_address(
            l1_address=ETH_ADDRESS
        )

        if response.sub_accounts:
            # Первый элемент - это ваш основной аккаунт
            account_index = response.sub_accounts[0].index
            print(f"Your ACCOUNT_INDEX: {account_index}")

            # Если есть субаккаунты
            for acc in response.sub_accounts:
                print(f"Account Index: {acc.index}")
        else:
            print("Account not found - you need to register on Lighter first")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        await api_client.close()


asyncio.run(get_account_index())