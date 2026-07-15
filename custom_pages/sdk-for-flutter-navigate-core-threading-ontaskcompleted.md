---
title: "OnTaskCompleted typedef - core.threading library - Dart API"
slug: "sdk-for-flutter-navigate-core-threading-ontaskcompleted"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core.threading/core.threading-library-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-typedef">OnTaskCompleted</span> typedef

</div>

<div class="section multi-line-signature">

<span class="name">OnTaskCompleted</span> = <span class="returntype">void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-taskOutcome" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-threading-taskoutcome">TaskOutcome</a></span> <span class="parameter-name">taskOutcome</span></span>)</span></span>

</div>

<div class="section desc markdown">

The method will be called on the main thread when a task call has been completed.

- `taskOutcome` The task outcome

</div>

## Implementation

``` dart
typedef OnTaskCompleted = void Function(TaskOutcome taskOutcome);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

