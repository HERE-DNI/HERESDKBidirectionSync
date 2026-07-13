---
title: "LocalizedTextPreference enum - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-localizedtextpreference"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/LocalizedTextPreference-enum-sidebar.html">

<div>

# <span class="kind-enum">LocalizedTextPreference</span> enum

</div>

<div class="section desc markdown">

Indicates the option of localized text usage.

</div>

## Values

<span class="name">useNever</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-localizedtextpreference">LocalizedTextPreference</a></span>  
Information is not included in the notification.

<span class="name">useAlways</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-localizedtextpreference">LocalizedTextPreference</a></span>  
Information is included in the notification, if available.

<span class="name">useIfLanguageIsCompatible</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-routing-localizedtextpreference">LocalizedTextPreference</a></span>  
Information is included in the notification, if available and its language code is compatible with the voice package language. For example, in case the voice package language is German and the localized text information is in Italian, the information is then excluded from the notification. More examples: \| Voice package language \| Information language \| Included \| \| en-GB \| en \| yes \| \| en-GB \| de \| no \| \| pt-BR \| pt \| yes \| \| pt-PT \| pt \| yes \|

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-routing-localizedtextpreference-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-localizedtextpreference-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-localizedtextpreference-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-localizedtextpreference-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-localizedtextpreference-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-routing-localizedtextpreference-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-routing-localizedtextpreference-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-localizedtextpreference">LocalizedTextPreference</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

