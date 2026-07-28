class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for aster in asteroids:
            while st and st[-1] > 0 and aster < 0:
                diff = aster + st[-1]
                if diff < 0:
                    st.pop()
                elif diff > 0:
                    aster = 0
                else:
                    aster = 0
                    st.pop()

            if aster:
                st.append(aster)
        
        return st