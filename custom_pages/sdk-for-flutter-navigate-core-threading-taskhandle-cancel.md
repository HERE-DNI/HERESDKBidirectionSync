---
title: "cancel method - TaskHandle class - core.threading library - Dart API"
slug: "sdk-for-flutter-navigate-core-threading-taskhandle-cancel"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core.threading/TaskHandle-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">cancel</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">bool</span> <span class="name">cancel</span>(<wbr></wbr>)

</div>

<div class="section desc markdown">

Sets internal state of task to 'canceled'.

If the task is still in the queue, it will be removed from it immediately. However, if the task is in a running state, it will nevertheless be completed, as there is no way to interrupt it.

Returns `bool`. True, if the task was canceled.

False, if the task can't be canceled due to a platform dependent reason.

</div>

## Implementation

``` dart
bool cancel();
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

