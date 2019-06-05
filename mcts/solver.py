from typing import List

from adi.fullnet import FullNet
from cube.model import Cube
from mcts.node_info import NodeInfo


class Solver:
    def __init__(self, net: FullNet):
        self._net = net
        self._set_hyper()

    def _set_hyper(self):
        self._loss_step = 0.1
        self._exploration_factor = 2.

    def solve(self, root: Cube) -> List[int]:
        self._initialize_tree(root)
        self._backup_stack = []

        while True:
            if self._traverse_for_solved():
                return self._extract_final_sequence(root)
            self._backup()

    def _initialize_tree(self, root: Cube):
        self._tree = dict()
        policy = self._net.evaluate(root.one_hot_encode().T)[0].policy
        self._tree[root] = NodeInfo.create_new(policy)

    def _traverse_for_solved(self) -> bool:
        pass

    def _backup(self):
        pass

    def _extract_final_sequence(self, root: Cube) -> List[int]:
        return BFSer().get_shortest_path_from(root, self._tree.keys())