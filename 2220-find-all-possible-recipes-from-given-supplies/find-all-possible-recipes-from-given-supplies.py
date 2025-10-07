from collections import defaultdict

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        active_ingredients = set(supplies)
        adj_list = defaultdict(list)

        for i, r in enumerate(recipes):
            reqs = ingredients[i]
            adj_list[r].extend(reqs)


        visiting = set()
        def dfs(ing):
            if ing in visiting and ing not in active_ingredients:
                return False

            visiting.add(ing)
            if ing in active_ingredients:
                visiting.remove(ing)
                return True
            elif ing in adj_list:
                for ing_req in adj_list[ing]:
                    if not dfs(ing_req):
                        visiting.remove(ing) 
                        return False
                active_ingredients.add(ing)

                visiting.remove(ing)
                return True
            else:
                visiting.remove(ing)
                return False

        return [r for r in recipes if dfs(r)]
