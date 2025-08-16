s = str(input())
p = str(input())

def construct_lsp(p: str) -> list[int]:
    lsp = [0]*len(p)

    length_counter = 0
    i = 1 

    while i < len(p):

        if p[length_counter] == p[i]:
            length_counter += 1
            lsp[i] = length_counter
            i += 1

        else:
            if length_counter == 0:
                i += 1
            else:
                length_counter = lsp[length_counter-1]
    return lsp


def kmp_matches(s:str, p:str) -> list[int]:
    n = len(s)
    m = len(p)
    outputs = []
    lsp = construct_lsp(p)

    i, j = 0, 0
        
    while i < n:
        if (s[i] == p[j]):
            i += 1
            j += 1
            
            if (j == m):
                outputs.append(i-m)
                j = lsp[j-1]
        else:
            if (j == 0):
                i += 1
            else:
                j = lsp[j-1]
    return outputs


print(kmp_matches(s,p))