---
title: "TaskHandle class - core.threading library - Dart API"
slug: "sdk-for-flutter-navigate-core.threading-taskhandle-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TaskHandle-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core.threading/core.threading-library-sidebar.html" data-below-sidebar="core.threading/TaskHandle-class-sidebar.html">

<div>

# <span class="kind-class">TaskHandle</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Handle used for the manipulation of the task.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-taskhandle">TaskHandle</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-cancelLambda" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">cancelLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-isFinishedGetLambda" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isFinishedGetLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-isCancelledGetLambda" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isCancelledGetLambda</span>()</span>)</span>  
Handle used for the manipulation of the task.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-iscancelled">isCancelled</a></span> <span class="signature">→ bool</span>  
Completion indication. True, if this task was canceled before it completed normally. Gets a boolean indicating if this task is cancelled.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-isfinished">isFinished</a></span> <span class="signature">→ bool</span>  
Completion indication. True, if this task is completed. Completion may be due to normal termination, an exception, or cancellation - in all of these cases, result will return `true`. Gets a boolean indicating if this task is completed.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-cancel">cancel</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ bool</span> </span>  
Sets internal state of task to 'canceled'.

<span class="name"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
