# Copyright (c) Alex Ponomarev.
# Distributed under the terms of the MIT License.


# Get the scale
def get(WIDTH, SCALE):
    nums = (WIDTH / 2)
    k = 1
    koeff = 1

    # Some magic to find the scale
    if nums // (SCALE / k) > 10:
        while nums // (SCALE / k) > 10:
            k /= 2
            koeff *= 2
            if nums // (SCALE / k) <= 10:
                break
            k /= 5
            koeff *= 2
    else:
        while nums // (SCALE / k) < 10:
            k *= 2
            if nums // (SCALE / k) >= 10:
                break
            k *= 5

    step = int((SCALE / k) * koeff)
    return step, koeff, k