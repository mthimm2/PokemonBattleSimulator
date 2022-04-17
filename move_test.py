import unittest
from move import Move
from copy import deepcopy

class test(unittest.TestCase):
    def test_move_name(self):
        
        # Create the move Dark Pulse
        a = Move(
            name = 'Dark Pulse',
            type = "Dark", 
            power = 80, 
            pp = 16, 
            multihit = False,
            can_flinch = True,
            flinch_rate = 30 ,
            physical_special_or_status = 1,
            stats_affected = None,
            forces_switch = False
        )
        self.assertEqual(a.name, 'Dark Pulse')

        # Create a nonsense move
        b = Move()
        self.assertEqual(b.name, '')
        b.name = 'Hurricane'
        self.assertEqual(b.name, 'Hurricane')
        self.assertNotEqual(b.name, '')
        self.assertNotEqual(b.name, 'Flamethrower')
        self.assertNotEqual(b.name, None)

        # Copy
        c = b
        self.assertEqual(c.name, 'Hurricane')
        c.name = 'Boomburst'
        self.assertEqual(c.name, 'Boomburst')
        
        # c isn't a deepcopy, so it modifies b
        self.assertEqual(b.name, 'Boomburst')

        # Deepcopy
        d = deepcopy(c)
        self.assertEqual(d.name, 'Boomburst')
        d.name = 'Bounce'
        self.assertNotEqual(d.name, b.name)
        self.assertNotEqual(d.name, c.name)


    def test_move_type(self):
        a = Move(
            name = 'Dark Pulse',
            type = "Dark", 
            power = 80, 
            pp = 16, 
            multihit = False,
            can_flinch = True,
            flinch_rate = 30 ,
            physical_special_or_status = 1,
            stats_affected = None,
            forces_switch = False
        )

        self.assertEqual(a.type, 'Dark')


    # def test_move_power(self):
    #     pass


    # def test_move_pp(self):
    #     pass


    # def test_move_multihit(self):
    #     pass


    # def test_move_physical_special_or_status(self):
    #     pass


    # def test_move_stats_affected(self):
    #     pass


    # def test_move_forces_switch(self):
    #     pass


if __name__ == '__main__':
    unittest.main()