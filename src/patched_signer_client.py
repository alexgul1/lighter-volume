"""
Патч для lighter.SignerClient - сброс синглтона перед созданием клиента.
Простое решение для независимых клиентов.
"""
import lighter
from typing import Dict, Optional
from lighter import nonce_manager


def reset_signer_singleton():
    """Сбрасывает глобальный синглтон в lighter.signer_client"""
    import lighter.signer_client as signer_module
    signer_module._SignerClient__signer = None


class PatchedSignerClient(lighter.SignerClient):
    """
    Патченный SignerClient - просто сбрасывает синглтон перед инициализацией.
    """

    def __init__(
            self,
            url,
            private_key,
            api_key_index,
            account_index,
            max_api_key_index=-1,
            private_keys: Optional[Dict[int, str]] = None,
            nonce_management_type=nonce_manager.NonceManagerType.OPTIMISTIC,
    ):
        # Сбросить синглтон перед созданием нового клиента
        reset_signer_singleton()
        
        # Вызвать оригинальный __init__
        super().__init__(
            url=url,
            private_key=private_key,
            api_key_index=api_key_index,
            account_index=account_index,
            max_api_key_index=max_api_key_index,
            private_keys=private_keys,
            nonce_management_type=nonce_management_type,
        )
