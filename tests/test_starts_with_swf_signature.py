from unittest import TestCase
from swf_firewall.swf_utils import starts_with_swf_signature


class TestStartsWithSwfSignature(TestCase):
    def test_should_return_true_for_data_starting_with_lzma_compression_swf_signature(self):
        self.assertTrue(starts_with_swf_signature(b"ZWSsome_data"))

    def test_should_return_false_for_data_containing_but_not_starting_with_lzma_compression_swf_signature(self):
        self.assertFalse(starts_with_swf_signature(b"some_ZWS_data"))

    def test_should_return_false_for_data_starting_with_lzma_compression_swf_signature_in_different_casing(self):
        # A swf signature for an LZMA compressed SWF is exactly the bytes
        # ZWS and not the same letters in any other casing
        self.assertFalse(starts_with_swf_signature(b"zWSsome_data"))

    def test_should_return_true_for_data_starting_with_zlib_compression_swf_signature(self):
        self.assertTrue(starts_with_swf_signature(b"CWSsome_data"))

    def test_should_return_false_for_data_containing_but_not_starting_with_zlib_compression_swf_signature(self):
        self.assertFalse(starts_with_swf_signature(b"some_CWS_data"))

    def test_should_return_false_for_data_starting_with_zlib_compression_swf_signature_in_different_casing(self):
        # A swf signature for an LZMA compressed SWF is exactly the bytes
        # CWS and not the same letters in any other casing
        self.assertFalse(starts_with_swf_signature(b"cWSsome_data"))

    def test_should_return_true_for_data_starting_with_no_compression_swf_signature(self):
        self.assertTrue(starts_with_swf_signature(b"FWSsome_data"))

    def test_should_return_false_for_data_containing_but_not_starting_with_no_compression_swf_signature(self):
        self.assertFalse(starts_with_swf_signature(b"some_FWS_data"))

    def test_should_return_false_for_data_starting_with_no_compression_swf_swf_signature_in_different_casing(self):
        self.assertFalse(starts_with_swf_signature(b"FwSsome_data"))

    def test_should_return_false_for_empty_data(self):
        self.assertFalse(starts_with_swf_signature(b""))