---
title: "LockingProcess class - core.engine library - Dart API"
slug: "sdk-for-flutter-navigate-core-engine-lockingprocess-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/LockingProcess-class-sidebar.html">

<div>

# <span class="kind-class">LockingProcess</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

LockingProcess helps to detect situations when cache is locked with another process and attempt to create instance of <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a> fails with error <a href="sdk-for-flutter-navigate-core-errors-instantiationerrorcode">InstantiationErrorCode.failedToLockCacheFolder</a>.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-lockingprocess-lockingprocess">LockingProcess</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-lockingprocess-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-lockingprocess-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-lockingprocess-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-lockingprocess-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-lockingprocess-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Static Methods

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-lockingprocess-destroylockingprocess">destroyLockingProcess</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-destroyLockingProcess-param-sdkOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdkoptions-class">SDKOptions</a></span> <span class="parameter-name">sdkOptions</span>, </span><span id="sdk-for-flutter-navigate-destroyLockingProcess-param-maxTimeoutInMilliseconds" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">maxTimeoutInMilliseconds</span></span>) <span class="returntype parameter">→ void</span> </span>  
Checks if cache folder is locked.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

