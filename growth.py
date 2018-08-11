import pygame, sys
import os
from pygame.locals import *
from random import *
import shelve

def grw(avars):

    grwch = [[16, 14, 17, 15, 17, 15],
             [20, 18, 21, 19, 21, 19],
             [[22, 24, 26], [22, 24, 26], 16, 14, 17, 15],
             [[23, 25, 27], [23, 25, 27], 20, 18, 21, 19],
             [22, 29, 14, 14, 14, 14],
             [23, 31, 20, 20, 20, 20],
             [32, 28, 22, 29, 14, 14],
             [33, 30, 23, 31, 20, 20],
             [24, 35, 16, 16, 16, 16],
             [25, 37, 19, 19, 19, 19],
             [38, 34, 24, 35, 16, 16],
             [39, 36, 25, 37, 19, 19],
             [26, 41, 15, 15, 15, 15],
             [27, 43, 21, 21, 21, 21],
             [44, 40, 26, 41, 15, 15],
             [45, 42, 27, 43, 21, 21],
             [[46, 52, 52], [48, 54, 54], [50, 56, 56]],
             [[52, 52, 52], [54, 54, 54], [56, 56, 56]],
             [[58, 64, 64], [60, 66, 66], [62, 68, 68]],
             [[64, 64, 64], [66, 66, 66], [68, 68, 68]],
             [[59, 65, 65], [61, 67, 67], [63, 69, 69]],
             [[65, 65, 65], [67, 67, 67], [69, 69, 69]],
             [[47, 53, 53], [49, 55, 55], [51, 57, 57]],
             [[53, 53, 53], [55, 55, 55], [57, 57, 57]],
             [[[70, 58, 64], [60, 60, 66], [62, 62, 68]], [[70, 46, 52], [48, 48, 54], [50, 50, 56]]],
             [[[71, 47, 53], [49, 49, 55], [51, 51, 57]], [[71, 59, 65], [61, 61, 67], [63, 63, 69]]],
             [[[58, 58, 64], [72, 60, 66], [62, 62, 68]], [[46, 46, 52], [72, 48, 54], [50, 50, 56]]],
             [[[47, 47, 53], [73, 49, 55], [51, 51, 57]], [[59, 59, 65], [73, 61, 67], [63, 63, 69]]],
             [[[58, 58, 64], [60, 60, 66], [74, 62, 68]], [[46, 46, 52], [48, 48, 54], [74, 50, 56]]],
             [[[47, 47, 53], [49, 49, 55], [75, 51, 57]], [[59, 59, 65], [61, 61, 67], [75, 63, 69]]], ###mame v
             [[58, 80, 46], [76, 52, 46], [78, 83, 46], [85, 87, 46]],
             [[80, 80, 46], [52, 52, 46], [83, 83, 46], [87, 87, 46]],
             [[59, 81, 47], [77, 82, 47], [79, 84, 47], [86, 53, 47]],
             [[81, 81, 47], [82, 82, 47], [84, 84, 47], [53, 53, 47]],
             [[88, 70, 46], [90, 94, 46], [92, 96, 46], [98, 100, 46]],
             [[89, 71, 47], [91, 95, 47], [93, 97, 47], [99, 101, 47]], ###meme v
             [[52, 76, 66], [102, 104, 66], [60, 62, 66], [106, 108, 66]],
             [[76, 76, 66], [104, 104, 66], [62, 62, 66], [108, 108, 66]],
             [[82, 77, 67], [103, 105, 67], [61, 63, 67], [107, 73, 67]],
             [[77, 77, 67], [105, 105, 67], [63, 63, 67], [73, 73, 67]],
             [[94, 90, 66], [109, 113, 66], [111, 115, 66], [72, 48, 66]],
             [[95, 91, 67], [110, 114, 67], [112, 116, 67], [117, 49, 67]], ###kuchi v
             [[83, 78, 56], [62, 60, 56], [118, 120, 56], [122, 124, 56]],
             [[78, 78, 56], [60, 60, 56], [120, 120, 56], [124, 124, 56]],
             [[84, 79, 57], [63, 61, 57], [119, 121, 57], [123, 51, 57]],
             [[79, 79, 57], [61, 61, 57], [121, 121, 57], [51, 51, 57]],
             [[96, 92, 56], [115, 111, 56], [125, 74, 56], [127, 68, 56]],
             [[97, 93, 57], [116, 112, 57], [126, 75, 57], [128, 129, 57]]]
#
    noneadults = [[[[202, 204, 206, 208, 210, 212],
                    [130, 132, 134, 136, 138, 140],
                    [142, 144, 146, 148, 150, 152],
                    [154, 156, 158, 160, 162, 164]], #Male odd
                   [[202, 204, 206, 208, 210, 212],
                    [166, 168, 170, 172, 174, 176],
                    [178, 180, 182, 184, 186, 188],
                    [190, 192, 194, 196, 198, 200]]], #Even
                  [[[203, 205, 207, 209, 211, 213],
                    [167, 169, 171, 173, 175, 177],
                    [179, 181, 183, 185, 187, 189],
                    [191, 193, 195, 197, 199, 201]], #Female odd
                   [[203, 205, 207, 209, 211, 213],
                    [131, 133, 135, 137, 139, 141],
                    [143, 145, 147, 149, 151, 153],
                    [155, 157, 159, 161, 163, 165]]]] #Even

    mameadults = [[[[214, 216, 218, 220, 222, 224],
                    [226, 228, 230, 232, 178, 234],
                    [166, 236, 238, 240, 242, 152]], #Male odd
                   [[244, 246, 248, 250, 252, 254],
                    [256, 258, 184, 260, 262, 264],
                    [202, 144, 266, 208, 268, 270]]], #Even
                  [[[215, 217, 219, 221, 223, 225],
                    [227, 229, 231, 233, 179, 235],
                    [167, 237, 239, 241, 243, 153]], #Female odd
                   [[245, 247, 249, 251, 253, 255],
                    [257, 259, 185, 261, 263, 265],
                    [203, 145, 267, 209, 269, 271]]]] #Even

    memeadults = [[[[272, 274, 276, 278, 280, 282],
                    [242, 284, 286, 236, 288, 180],
                    [178, 290, 182, 228, 174, 292]], #Male odd
                   [[294, 296, 298, 300, 302, 304],
                    [268, 306, 308, 144, 310, 312],
                    [262, 204, 314, 258, 210, 316]]], #Even
                  [[[273, 275, 277, 279, 281, 283],
                    [243, 285, 287, 237, 289, 181],
                    [179, 205, 291, 229, 211, 293]], #Female odd
                   [[295, 297, 299, 301, 303, 305],
                    [269, 307, 309, 145, 311, 313],
                    [263, 169, 183, 259, 315, 317]]]] #Even

    kuchiadults = [[[[318, 320, 322, 324, 326, 328],
                    [152, 292, 330, 238, 182, 332],
                    [234, 180, 170, 230, 286, 334]], #Male odd
                   [[336, 338, 340, 342, 344, 346],
                    [270, 316, 348, 266, 314, 350],
                    [264, 312, 206, 184, 308, 212]]], #Even
                  [[[319, 321, 323, 325, 327, 329],
                    [153, 293, 331, 239, 291, 333],
                    [235, 181, 171, 231, 287, 335]], #Female odd
                   [[337, 339, 341, 343, 345, 347],
                    [271, 317, 349, 267, 183, 351],
                    [265, 313, 207, 185, 309, 213]]]] #Even

    if (1 < avars[avars[3][5]][1]) and (len(avars[3]) > 10):
        a = avars[avars[3][5]][24]
        a.append(avars[avars[3][5]][15])
        avars[avars[3][5]][24] = a

    if avars[avars[3][5]][11] in ["ma", "me", "ku", "no"]:
        if avars[avars[3][5]][1] == 1:
            
            if int(avars[avars[3][5]][0]) == 1:
                ch = 3
                if avars[avars[3][5]][13] == "ma":
                    avars[avars[3][5]][5] += 1
                    avars[avars[3][5]][8] += 1
                if avars[avars[3][5]][13] == "me":
                    avars[avars[3][5]][6] += 1
                    avars[avars[3][5]][9] += 1
                if avars[avars[3][5]][13] == "ku":
                    avars[avars[3][5]][7] += 1
                    avars[avars[3][5]][10] += 1
            if int(avars[avars[3][5]][0]) == 2:
                ch = 5
                avars[avars[3][5]][5] += 1
                avars[avars[3][5]][8] += 1
            if int(avars[avars[3][5]][0]) == 3:
                ch = 15
                avars[avars[3][5]][7] += 1
                avars[avars[3][5]][10] += 1
            if int(avars[avars[3][5]][0]) == 4:
                ch = 13
                avars[avars[3][5]][7] += 1
                avars[avars[3][5]][10] += 1
            if int(avars[avars[3][5]][0]) == 5:
                ch = 7
                avars[avars[3][5]][5] += 1
                avars[avars[3][5]][8] += 1
            if int(avars[avars[3][5]][0]) == 6:
                ch = 11
                avars[avars[3][5]][6] += 1
                avars[avars[3][5]][9] += 1
            if int(avars[avars[3][5]][0]) == 7:
                ch = 9
                avars[avars[3][5]][6] += 1
                avars[avars[3][5]][9] += 1
            if int(avars[avars[3][5]][0]) == 8:
                ch = 1
            gen = avars[avars[3][5]][14] % 2
            ch += gen
            g = avars[avars[3][5]][14]
            if g < 0:
                g = 4294967296 + g
            a = format(g, '032b')
            if a[9:11] + a[16:18] == '1111':
                avars[avars[3][5]][5] += 10
            if a[1:3] + a[18:20] == '1111':
                avars[avars[3][5]][6] += 10
            if a[5:7] + a[20:22] == '1111':
                avars[avars[3][5]][7] += 10
            if a[3:5] + a[22:24] == '1111':
                avars[avars[3][5]][8] += 10
            if a[7:9] + a[24:26] == '1111':
                avars[avars[3][5]][9] += 10
            if a[0] + a[11] + a[26:28] == '1111':
                avars[avars[3][5]][10] += 10
            avars[avars[3][5]][15] = ch

        elif avars[avars[3][5]][1] == 2:
            cm = 2 * (avars[avars[3][5]][19] // 2)
            if (avars[avars[3][5]][18] > 24 or avars[avars[3][5]][18] < 5) and cm < 4:
                cm += 2
                if avars[avars[3][5]][18] > 44 and cm < 4:
                    cm += 2
            if avars[avars[3][5]][4] > 3 and cm < 4:
                cm += 2
            mapt = avars[avars[3][5]][5] + avars[avars[3][5]][8]
            mept = avars[avars[3][5]][6] + avars[avars[3][5]][9]
            kupt = avars[avars[3][5]][7] + avars[avars[3][5]][10]
            apt = avars[avars[3][5]][5] + avars[avars[3][5]][8] + avars[avars[3][5]][6] + avars[avars[3][5]][9] + avars[avars[3][5]][7] + avars[avars[3][5]][10]
            if ((avars[avars[3][5]][15] == 7 or avars[avars[3][5]][15] == 8) and (mapt < 10 or apt < 20)) or ((avars[avars[3][5]][15] == 11 or avars[avars[3][5]][15] == 12) and (mept < 10 or apt < 20)) or ((avars[avars[3][5]][15] == 15 or avars[avars[3][5]][15] == 16) and (kupt < 10 or apt < 20)):
                if cm == 0:
                    cm = 2
            genn = int(2 * ((avars[avars[3][5]][3] / 2) - (avars[avars[3][5]][3] // 2)))
            if (avars[avars[3][5]][15] == 3 or avars[avars[3][5]][15] == 4) and cm == 0:
                if (avars[avars[3][5]][12] == "ma" or avars[avars[3][5]][13] == "ma") and mapt > 19:
                    avars[avars[3][5]][15] = grwch[(avars[avars[3][5]][15] - 1)][cm][0]
                elif (avars[avars[3][5]][12] == "me" or avars[avars[3][5]][13] == "me") and mept > 19:
                    avars[avars[3][5]][15] = grwch[(avars[avars[3][5]][15] - 1)][cm][1]
                elif (avars[avars[3][5]][12] == "ku" or avars[avars[3][5]][13] == "ku") and kupt > 19:
                    avars[avars[3][5]][15] = grwch[(avars[avars[3][5]][15] - 1)][cm][2]
                else:
                    cm = 2
                    avars[avars[3][5]][15] = grwch[(avars[avars[3][5]][15] - 1)][(cm + genn)]
            else:
                avars[avars[3][5]][15] = grwch[(avars[avars[3][5]][15] - 1)][(cm + genn)]
            avars[avars[3][5]][5] += 1
            avars[avars[3][5]][6] += 1
            avars[avars[3][5]][7] += 1
            avars[avars[3][5]][8] += 1
            avars[avars[3][5]][9] += 1
            avars[avars[3][5]][10] += 1

        elif avars[avars[3][5]][1] == 3:
            cm = (avars[avars[3][5]][19] // 2)
            if (avars[avars[3][5]][18] > 39 or avars[avars[3][5]][18] < 10) and cm < 2:
                cm += 1
                if avars[avars[3][5]][18] > 59 and cm < 2:
                    cm += 1
            if avars[avars[3][5]][4] > 3 and cm < 2:
                cm += 1
            mapt = avars[avars[3][5]][5] + avars[avars[3][5]][8]
            mept = avars[avars[3][5]][6] + avars[avars[3][5]][9]
            kupt = avars[avars[3][5]][7] + avars[avars[3][5]][10]
            apt = avars[avars[3][5]][5] + avars[avars[3][5]][8] + avars[avars[3][5]][6] + avars[avars[3][5]][9] + avars[avars[3][5]][7] + avars[avars[3][5]][10]
            if apt < 100 and cm < 2:
                cm += 1
            genn = int(2 * ((avars[avars[3][5]][3] / 2) - (avars[avars[3][5]][3] // 2)))
            if avars[avars[3][5]][11] == "no":
                gl = [mapt, mept, kupt]
                m = max(gl)
                l = []
                for i in range(0, 3):
                    if gl[i] == m:
                        l.append(i)
                gts = choice(l)
                if avars[avars[3][5]][15] < 25:
                    avars[avars[3][5]][15] = grwch[(avars[avars[3][5]][15] - 1)][gts][cm]
                else:
                    avars[avars[3][5]][15] = grwch[(avars[avars[3][5]][15] - 1)][genn][gts][cm]
            elif avars[avars[3][5]][11] == "ma":
                gl = [avars[avars[3][5]][5], mept, kupt, avars[avars[3][5]][8]]
                m = max(gl)
                l = []
                for i in range(0, 4):
                    if gl[i] == m:
                        l.append(i)
                gts = choice(l)
                if avars[avars[3][5]][15] == 17:
                    avars[avars[3][5]][15] = 46
                elif avars[avars[3][5]][15] == 23:
                    avars[avars[3][5]][15] = 47
                else:
                    if avars[avars[3][5]][15] < 31:
                        avars[avars[3][5]][15] += 10
                        if cm == 0:
                            cm = 1
                    avars[avars[3][5]][15] = grwch[(avars[avars[3][5]][15] - 1)][gts][cm]
            elif avars[avars[3][5]][11] == "me":
                gl = [mapt, avars[avars[3][5]][6], kupt, avars[avars[3][5]][9]]
                m = max(gl)
                l = []
                for i in range(0, 4):
                    if gl[i] == m:
                        l.append(i)
                gts = choice(l)
                if avars[avars[3][5]][15] == 19:
                    avars[avars[3][5]][15] = 66
                elif avars[avars[3][5]][15] == 22:
                    avars[avars[3][5]][15] = 67
                else:
                    if avars[avars[3][5]][15] < 31:
                        avars[avars[3][5]][15] += 14
                        if cm == 0:
                            cm = 1
                    avars[avars[3][5]][15] = grwch[(avars[avars[3][5]][15] - 1)][gts][cm]
            elif avars[avars[3][5]][11] == "ku":
                gl = [mapt, mept, avars[avars[3][5]][7], avars[avars[3][5]][10]]
                m = max(gl)
                l = []
                for i in range(0, 4):
                    if gl[i] == m:
                        l.append(i)
                gts = choice(l)
                if avars[avars[3][5]][15] == 18:
                    avars[avars[3][5]][15] = 56
                elif avars[avars[3][5]][15] == 24:
                    avars[avars[3][5]][15] = 57
                else:
                    if avars[avars[3][5]][15] < 31:
                        avars[avars[3][5]][15] += 18
                        if cm == 0:
                            cm = 1
                    avars[avars[3][5]][15] = grwch[(avars[avars[3][5]][15] - 1)][gts][cm]
            avars[avars[3][5]][5] += 5
            avars[avars[3][5]][6] += 5
            avars[avars[3][5]][7] += 5
            avars[avars[3][5]][8] += 5
            avars[avars[3][5]][9] += 5
            avars[avars[3][5]][10] += 5

        elif avars[avars[3][5]][1] == 4:
            cm = (avars[avars[3][5]][19] // 2)
            if (avars[avars[3][5]][18] > 59 or avars[avars[3][5]][18] < 20) and cm < 2:
                cm += 1
                if avars[avars[3][5]][18] > 79 and cm < 2:
                    cm += 1
            if avars[avars[3][5]][4] > 3 and cm < 2:
                cm += 1
            if avars[avars[3][5]][33] < 4 and cm < 2:
                cm += 1
            apt = avars[avars[3][5]][5] + avars[avars[3][5]][8] + avars[avars[3][5]][6] + avars[avars[3][5]][9] + avars[avars[3][5]][7] + avars[avars[3][5]][10]
            if apt < 500 and cm < 2:
                cm += 1
            gl = [avars[avars[3][5]][5], avars[avars[3][5]][6], avars[avars[3][5]][7], avars[avars[3][5]][8], avars[avars[3][5]][9], avars[avars[3][5]][10]]
            m = max(gl)
            l = []
            for i in range(0, 6):
                if gl[i] == m:
                    l.append(i)
            gts = choice(l)
            genn = not(avars[avars[3][5]][3] % 2)
            gen = avars[avars[3][5]][14] % 2
            if avars[avars[3][5]][11] == "no":
                if avars[avars[3][5]][15] not in range(73, 79):
                    cm += (1 + (cm == 0 and ((avars[avars[3][5]][15] - 3) != [[46, 58], [59, 47], [48, 60], [61, 49], [50, 62], [63, 51]][((gts % 3) * 2) + gen][genn])))
                    if (avars[avars[3][5]][15] - 3) in [52, 53, 54, 55, 56, 57, 64, 65, 66, 67, 68, 69]:
                        cm = 3
                elif avars[avars[3][5]][15] != range(73, 79)[(((gts % 3) * 2) + gen)]:
                    cm += (1 + (cm == 0))
                if cm == 0:
                    avars[avars[3][5]][12] = ["ma", "me", "ku"][gts % 3]
                elif cm == 1:
                    avars[avars[3][5]][13] = ["ma", "me", "ku"][gts % 3]
                avars[avars[3][5]][15] = noneadults[gen][genn][cm][gts]
            elif avars[avars[3][5]][11] == "ma":
                if avars[avars[3][5]][15] in [49, 50]:
                    if cm == 0 and gts in [0, 3]:
                        avars[avars[3][5]][15] += 81
                    else:
                        avars[avars[3][5]][15] += 105
                        avars[avars[3][5]][13] = "no"
                else:
                    s = [0, 1, 2, 3, 1, 2][gts]
                    if (avars[avars[3][5]][15] - 3) in [80, 81, 52, 82, 83, 84, 87, 53, 70, 71, 94, 95, 96, 97, 100, 101]:
                        cm += (1 + (cm == 0))
                    elif (avars[avars[3][5]][15] - 3) != grwch[[[30, 34], [32, 35]][gen][genn]][s][0]:
                        cm += (cm == 0)
                    if cm > 2:
                        avars[avars[3][5]][15] = [154, 155][gen]
                        avars[avars[3][5]][13] = "no"
                    else:
                        avars[avars[3][5]][15] = mameadults[gen][genn][cm][gts]
            elif avars[avars[3][5]][11] == "me":
                if avars[avars[3][5]][15] in [69, 70]:
                    if cm == 0 and gts in [1, 4]:
                        avars[avars[3][5]][15] += 69
                    else:
                        avars[avars[3][5]][15] += 87
                        avars[avars[3][5]][13] = "no"
                else:
                    s = [0, 1, 2, 0, 3, 2][gts]
                    if (avars[avars[3][5]][15] - 3) in [76, 77, 104, 105, 62, 63, 108, 73, 90, 91, 113, 114, 115, 116, 48, 49]:
                        cm += (1 + (cm == 0))
                    elif (avars[avars[3][5]][15] - 3) != grwch[[[36, 40], [38, 41]][gen][genn]][s][0]:
                        cm += (cm == 0)
                    if cm > 2:
                        avars[avars[3][5]][15] = [156, 157][gen]
                        avars[avars[3][5]][13] = "no"
                    else:
                        avars[avars[3][5]][15] = memeadults[gen][genn][cm][gts]
            elif avars[avars[3][5]][11] == "ku":
                if avars[avars[3][5]][15] in [59, 60]:
                    if cm == 0 and gts in [2, 5]:
                        avars[avars[3][5]][15] += 75
                    else:
                        avars[avars[3][5]][15] += 99
                        avars[avars[3][5]][13] = "no"
                else:
                    s = [0, 1, 2, 0, 1, 3][gts]
                    if (avars[avars[3][5]][15] - 3) in [78, 79, 60, 61, 120, 121, 124, 51, 92, 93, 111, 112, 74, 75, 68, 129]:
                        cm += (1 + (cm == 0))
                    elif (avars[avars[3][5]][15] - 3) != grwch[[[42, 46], [44, 47]][gen][genn]][s][0]:
                        cm += (cm == 0)
                    if cm > 2:
                        avars[avars[3][5]][15] = [158, 159][gen]
                        avars[avars[3][5]][13] = "no"
                    else:
                        avars[avars[3][5]][15] = kuchiadults[gen][genn][cm][gts]
            if avars[avars[3][5]][18] == 99:
                avars[avars[3][5]][15] = [372, 373][gen]
            elif avars[avars[3][5]][18] == 1:
                avars[avars[3][5]][15] = [374, 375][gen]
            avars[avars[3][5]][5] += 20
            avars[avars[3][5]][6] += 20
            avars[avars[3][5]][7] += 20
            avars[avars[3][5]][8] += 20
            avars[avars[3][5]][9] += 20
            avars[avars[3][5]][10] += 20

        elif avars[avars[3][5]][1] == 5:
            avars[avars[3][5]][15] = 355 + [163, 194, 187, 154, 193, 166, 167, 204,
                                            217, 248, 253, 224, 299, 278, 283, 306, 325, 344, 349, 332].index(avars[avars[3][5]][15])

        elif avars[avars[3][5]][1] == 6:
            if avars[avars[3][5]][11] == "no":
                mapt = avars[avars[3][5]][5] + avars[avars[3][5]][8]
                mept = avars[avars[3][5]][6] + avars[avars[3][5]][9]
                kupt = avars[avars[3][5]][7] + avars[avars[3][5]][10]
                gl = [mapt, mept, kupt]
                m = max(gl)
                l = []
                for i in range(0, 3):
                    if gl[i] == m:
                        l.append(i)
                gts = choice(l)
                gen = avars[avars[3][5]][14] % 2
                avars[avars[3][5]][15] = 379 + (2 * gts) + gen
            elif avars[avars[3][5]][11] == "ma":
                gen = avars[avars[3][5]][14] % 2
                avars[avars[3][5]][15] = 379 + gen
            elif avars[avars[3][5]][11] == "me":
                gen = avars[avars[3][5]][14] % 2
                avars[avars[3][5]][15] = 381 + gen
            elif avars[avars[3][5]][11] == "ku":
                gen = avars[avars[3][5]][14] % 2
                avars[avars[3][5]][15] = 383 + gen

        if 1 < avars[avars[3][5]][1] < 5:
            avars[avars[3][5]][15] += 3

        if len(avars[3]) > 10:
            x = avars[3][23]
            x = format(x, '0384b')
            x = x[:(avars[avars[3][5]][15] - 1)] + '1' + x[avars[avars[3][5]][15]:]
            avars[3][23] = int(x, 2)
    else:
        n = open(("CCharacters/" + avars[avars[3][5]][11] + ".txt"), 'r')
        t = n.read()
        t = t.split('/')
        for i in range(1, len(t)):
            t[i] = t[i].split("-")
        cm = (avars[avars[3][5]][19] // 2)
        mapt = avars[avars[3][5]][5] + avars[avars[3][5]][8]
        mept = avars[avars[3][5]][6] + avars[avars[3][5]][9]
        kupt = avars[avars[3][5]][7] + avars[avars[3][5]][10]
        apt = avars[avars[3][5]][5] + avars[avars[3][5]][8] + avars[avars[3][5]][6] + avars[avars[3][5]][9] + avars[avars[3][5]][7] + avars[avars[3][5]][10]
        g = avars[avars[3][5]][14]
        if g < 0:
            g = 4294967296 + g
        if avars[avars[3][5]][1] == 1:
            a = format(g, '032b')
            if a[9:11] + a[16:18] == '1111':
                avars[avars[3][5]][5] += 10
            if a[1:3] + a[18:20] == '1111':
                avars[avars[3][5]][6] += 10
            if a[5:7] + a[20:22] == '1111':
                avars[avars[3][5]][7] += 10
            if a[3:5] + a[22:24] == '1111':
                avars[avars[3][5]][8] += 10
            if a[7:9] + a[24:26] == '1111':
                avars[avars[3][5]][9] += 10
            if a[0] + a[11] + a[26:28] == '1111':
                avars[avars[3][5]][10] += 10
            avars[avars[3][5]][15] = int(t[1][g % 2])
        elif avars[avars[3][5]][1] == 2:
            cm *= 2
            if (avars[avars[3][5]][18] > 24 or avars[avars[3][5]][18] < 5) and cm < 4:
                cm += 2
                if avars[avars[3][5]][18] > 44 and cm < 4:
                    cm += 2
            if avars[avars[3][5]][4] > 3 and cm < 4:
                cm += 2
            avars[avars[3][5]][15] = int(t[2][((cm > 1) * 2) + (g % 2)])
            avars[avars[3][5]][5] += 1
            avars[avars[3][5]][6] += 1
            avars[avars[3][5]][7] += 1
            avars[avars[3][5]][8] += 1
            avars[avars[3][5]][9] += 1
            avars[avars[3][5]][10] += 1
        elif avars[avars[3][5]][1] == 3:
            if (avars[avars[3][5]][18] > 39 or avars[avars[3][5]][18] < 10) and cm < 2:
                cm += 1
                if avars[avars[3][5]][18] > 59 and cm < 2:
                    cm += 1
            if avars[avars[3][5]][4] > 3 and cm < 2:
                cm += 1
            if (apt < 100 or (avars[avars[3][5]][15] in t[2][2:])) and cm < 2:
                cm += 1
            gl = [mapt, mept, kupt]
            m = max(gl)
            l = []
            for i in range(0, 3):
                if gl[i] == m:
                    l.append(i)
            gts = choice(l)
            avars[avars[3][5]][15] = int(t[3][((cm > 0) * 6) + (2 * gts) + (g % 2)])
            avars[avars[3][5]][5] += 5
            avars[avars[3][5]][6] += 5
            avars[avars[3][5]][7] += 5
            avars[avars[3][5]][8] += 5
            avars[avars[3][5]][9] += 5
            avars[avars[3][5]][10] += 5
        elif avars[avars[3][5]][1] == 4:
            if (avars[avars[3][5]][18] > 59 or avars[avars[3][5]][18] < 20) and cm < 2:
                cm += 1
                if avars[avars[3][5]][18] > 79 and cm < 2:
                    cm += 1
            if avars[avars[3][5]][4] > 3 and cm < 2:
                cm += 1
            if avars[avars[3][5]][33] < 4 and cm < 2:
                cm += 1
            apt = avars[avars[3][5]][5] + avars[avars[3][5]][8] + avars[avars[3][5]][6] + avars[avars[3][5]][9] + avars[avars[3][5]][7] + avars[avars[3][5]][10]
            if apt < 500 and cm < 2:
                cm += 1
            if (avars[avars[3][5]][15] in t[3][6:]):
                cm = 2
            gl = [avars[avars[3][5]][5], avars[avars[3][5]][6], avars[avars[3][5]][7], avars[avars[3][5]][8], avars[avars[3][5]][9], avars[avars[3][5]][10]]
            m = max(gl)
            l = []
            for i in range(0, 6):
                if gl[i] == m:
                    l.append(i)
            gts = choice(l)
            if (avars[avars[3][5]][15] not in t[3][(2 * (gts % 3)):(2 * ((gts % 3) + 1))]) and cm == 0:
                cm = 1
            avars[avars[3][5]][15] = int(t[4][(cm * 12) + (2 * gts) + (g % 2)])
            avars[avars[3][5]][5] += 20
            avars[avars[3][5]][6] += 20
            avars[avars[3][5]][7] += 20
            avars[avars[3][5]][8] += 20
            avars[avars[3][5]][9] += 20
            avars[avars[3][5]][10] += 20
        elif avars[avars[3][5]][1] == 6:
            avars[avars[3][5]][15] = int(t[5][(g % 2)])

    print(avars[avars[3][5]][15])

    return(avars)
