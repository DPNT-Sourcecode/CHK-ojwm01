from solutions.CHK import checkout_solution


class TestChk():
    def test_singles(self):
        assert checkout_solution.checkout('ABCDE') == 155

    def test_offers(self):
        assert checkout_solution.checkout('AAAAAAAAAAAAAAAA') == 300
        assert checkout_solution.checkout('AAAAAAAA') == 430
        assert checkout_solution.checkout('BBB') == 75
        assert checkout_solution.checkout('EEEBBB') == 165

    def test_no_sku(self):
        assert checkout_solution.checkout('AB') == 80

    def test_illegal_input(self):
        assert checkout_solution.checkout('A,B,C,D') == -1
        assert checkout_solution.checkout(["ABCa"]) == -1
        assert checkout_solution.checkout(["-"]) == -1

    # def test_string_format(self):
    #     assert checkout_solution.checkout('ABCD') == 115
    #     assert checkout_solution.checkout('A;B;C;D') == 115