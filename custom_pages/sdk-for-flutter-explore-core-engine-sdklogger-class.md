---
title: "SDKLogger class - core.engine library - Dart API"
slug: "sdk-for-flutter-explore-core-engine-sdklogger-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="core.engine/core.engine-library-sidebar.html" data-below-sidebar="core.engine/SDKLogger-class-sidebar.html">

<div>

# <span class="kind-class">SDKLogger</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Logging interface for Android/iOS platforms.

These logs are under management of <a href="sdk-for-flutter-explore-core-engine-logcontrol-class">LogControl</a> and should be used instead of platform-specific logging functions.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-core-engine-sdklogger-sdklogger">SDKLogger</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-core-engine-sdklogger-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-sdklogger-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-core-engine-sdklogger-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-sdklogger-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-core-engine-sdklogger-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Static Methods

<span class="name"><a href="sdk-for-flutter-explore-core-engine-sdklogger-error">error</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-error-param-tag" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">tag</span>, </span><span id="sdk-for-flutter-explore-error-param-message" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">message</span></span>) <span class="returntype parameter">→ void</span> </span>  
convenient function to print a message with log level ERROR and tag.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-sdklogger-fatal">fatal</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-fatal-param-tag" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">tag</span>, </span><span id="sdk-for-flutter-explore-fatal-param-message" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">message</span></span>) <span class="returntype parameter">→ void</span> </span>  
convenient function to print a message with log level FATAL and tag.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-sdklogger-info">info</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-info-param-tag" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">tag</span>, </span><span id="sdk-for-flutter-explore-info-param-message" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">message</span></span>) <span class="returntype parameter">→ void</span> </span>  
convenient function to print a message with log level INFO and tag.

<span class="name"><a href="sdk-for-flutter-explore-core-engine-sdklogger-log">log</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-log-param-level" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-core-engine-loglevel">LogLevel</a></span> <span class="parameter-name">level</span>, </span><span id="sdk-for-flutter-explore-log-param-tag" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">tag</span>, </span><span id="sdk-for-flutter-explore-log-param-message" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">message</span></span>) <span class="returntype parameter">→ void</span> </span>  
<li>

`level` The severity of the log message.

</li>

<li>

`tag` The log tag.

</li>

<li>

`message` The log message.

</li>

<span class="name"><a href="sdk-for-flutter-explore-core-engine-sdklogger-warn">warn</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-warn-param-tag" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">tag</span>, </span><span id="sdk-for-flutter-explore-warn-param-message" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">message</span></span>) <span class="returntype parameter">→ void</span> </span>  
convenient function to print a message with log level WARNING and tag.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

