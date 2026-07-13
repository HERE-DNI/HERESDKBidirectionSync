---
title: "LogControl class - core.engine library - Dart API"
slug: "sdk-for-flutter-navigate-core.engine-logcontrol-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/LogControl-class-sidebar.html">

<div>

# <span class="kind-class">LogControl</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

This class provides functionality to enable/disable console logs as well as setting a custom log appender to receive log messages from the SDK.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-logcontrol-logcontrol">LogControl</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-logcontrol-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-logcontrol-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-logcontrol-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-logcontrol-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-logcontrol-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Static Methods

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-logcontrol-disableloggingtoconsole">disableLoggingToConsole</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Disables SDK logging messages to console.

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-logcontrol-enableloggingtoconsole">enableLoggingToConsole</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-enableLoggingToConsole-param-level" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-loglevel">LogLevel</a></span> <span class="parameter-name">level</span></span>) <span class="returntype parameter">→ void</span> </span>  
Enables SDK logging messages to console .

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-logcontrol-removeappender">removeAppender</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Removes previously added custom log appender.

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-logcontrol-setappender">setAppender</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setAppender-param-level" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-loglevel">LogLevel</a></span> <span class="parameter-name">level</span>, </span><span id="sdk-for-flutter-navigate-setAppender-param-path" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">path</span></span>) <span class="returntype parameter">→ void</span> </span>  
Sets a custom log appender that will write SDK log messages to a file.

<span class="name"><a href="sdk-for-flutter-navigate-core-engine-logcontrol-setcustomappender">setCustomAppender</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setCustomAppender-param-level" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-loglevel">LogLevel</a></span> <span class="parameter-name">level</span>, </span><span id="sdk-for-flutter-navigate-setCustomAppender-param-appender" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-logappender-class">LogAppender</a></span> <span class="parameter-name">appender</span></span>) <span class="returntype parameter">→ void</span> </span>  
Sets a custom log appender to receive log messages from the SDK.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

