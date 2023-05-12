# AI Image Recognition Tool
**Heavy work in  progress, performance may vary on computers**

Aimed to help the visually impaired, this tool allows users to put images on their screen
through an AI image recognition model, which then will use text-to-speech to express that object. **This tool will never store any data or pictures that are sent through the model.**

This program uses **Ultralytics YOLO8**, the acclaimed real-time object detection and image segmentation model.
This tool would not have been possible without it, and you can access it here:
https://github.com/ultralytics/ultralytics

The object/image dataset used for the model is **COCO** (Common Objects in Context - https://cocodataset.org/),
which only roughly 80 object categories. More categories will be added in the near future.

Currently, these are the following categories:
1. bicycle 
2. car  
3. motorcycle  
4. airplane  
5. bus  
6. train 
7. truck
8. boat 
9. traffic light 
10. fire hydrant 
11. stop sign 
12. parking meter 
13. bench
14. bird 
15. cat 
16. dog 
17. horse 
18. sheep 
19. cow 20. elephant 21. bear
22. zebra 
23. giraffe 
24. backpack 
25. umbrella 
26. handbag 
27. tie 
28. suitcase
29. frisbee 
30. skis 
31. snowboard 
32. sports ball 
33. kite 
34. baseball bat
35. baseball glove 
36. skateboard 
37. surfboard 
38. tennis racket 
39. bottle
40. wine glass 
41. cup 
42. fork 
43. knife 
44. spoon 
45. bowl 
46. banana 
47. apple
48. sandwich 
49. orange 
50. broccoli 
51. carrot 
52. hot dog 
53. pizza 
54. donut
55. cake 
56. chair 
57. couch 
58. potted plant 
59. bed 
60. dining table 
61. toilet
62. tv 
63. laptop 
64. mouse 
65. remote 
66. keyboard 
67. cell phone 
68. microwave
69. oven 
70. toaster 
71. sink 
72. refrigerator 
73. book 
74. clock 
75. vase
76. scissors 
77. teddy bear 
78. hair drier 
79. toothbrush
