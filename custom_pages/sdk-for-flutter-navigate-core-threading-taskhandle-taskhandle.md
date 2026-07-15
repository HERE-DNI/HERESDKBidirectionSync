---
title: "TaskHandle constructor - TaskHandle - core.threading library - Dart API"
slug: "sdk-for-flutter-navigate-core-threading-taskhandle-taskhandle"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core.threading/TaskHandle-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">TaskHandle</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">TaskHandle</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-param-cancelLambda" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">cancelLambda</span>(), </span>
2.  <span id="sdk-for-flutter-navigate-param-isFinishedGetLambda" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isFinishedGetLambda</span>(), </span>
3.  <span id="sdk-for-flutter-navigate-param-isCancelledGetLambda" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isCancelledGetLambda</span>()</span>

)

</div>

<div class="section desc markdown">

Handle used for the manipulation of the task.

</div>

## Implementation

``` dart
factory TaskHandle(
  bool Function() cancelLambda,
  bool Function() isFinishedGetLambda,
  bool Function() isCancelledGetLambda
) => TaskHandle$Lambdas(
  cancelLambda,
  isFinishedGetLambda,
  isCancelledGetLambda
);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

