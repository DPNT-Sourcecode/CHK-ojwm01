from solutions.CHK import checkout_solution


class TestChk():
    def test_singles(self):
        assert checkout_solution.checkout('ABCDEFGHIJKLMNOPQRSTUVWXYZ') == 965

    def test_offers(self):
        assert checkout_solution.checkout('AAAAAAAAAAAAAAA') == 600
        assert checkout_solution.checkout('AAAAAAAA') == 330
        assert checkout_solution.checkout('BBB') == 75
        assert checkout_solution.checkout('EEEBBB') == 165
        assert checkout_solution.checkout("EEEFFFB") == 140
        assert checkout_solution.checkout("FF") == 20
        assert checkout_solution.checkout("HHHHHHHHHHHHHHH") == 125
        assert checkout_solution.checkout("KKK") == 230
        assert checkout_solution.checkout("NNNM") == 120
        assert checkout_solution.checkout("UUUU") == 120
        assert checkout_solution.checkout("VVVVVVVV") == 350

    def test_no_sku(self):
        assert checkout_solution.checkout('AB') == 80

    def test_illegal_input(self):
        assert checkout_solution.checkout('A,B,C,D') == -1
        assert checkout_solution.checkout(["ABCa"]) == -1
        assert checkout_solution.checkout(["-"]) == -1

    # def test_string_format(self):
    #     assert checkout_solution.checkout('ABCD') == 115
    #     assert checkout_solution.checkout('A;B;C;D') == 115
