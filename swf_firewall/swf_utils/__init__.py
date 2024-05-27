NO_COMPRESSION_SWF_SIGNATURE = b"FWS"
ZLIB_COMPRESSION_SWF_SIGNATURE = b"CWS"
LZMA_COMPRESSION_SWF_SIGNATURE = b"ZWS"


def starts_with_swf_signature(data: bytes) -> bool:
    """Checks if the given data starts with any of the 3 SWF signatures"""
    swf_signatures = [
        NO_COMPRESSION_SWF_SIGNATURE,
        ZLIB_COMPRESSION_SWF_SIGNATURE,
        LZMA_COMPRESSION_SWF_SIGNATURE]
    return any(data.startswith(swf_signature) for swf_signature in swf_signatures)

