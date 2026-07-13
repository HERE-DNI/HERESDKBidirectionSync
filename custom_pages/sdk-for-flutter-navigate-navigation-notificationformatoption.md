---
title: "NotificationFormatOption enum - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-notificationformatoption"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- NotificationFormatOption.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/NotificationFormatOption-enum-sidebar.html">

<div>

# <span class="kind-enum">NotificationFormatOption</span> enum

</div>

<div class="section desc markdown">

Indicates the formatting option of phoneme included in the notification.

</div>

## Values

<span class="name">plain</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-navigation-notificationformatoption">NotificationFormatOption</a></span>  
No phoneme is used for this option as plain orthographic form is included in the notification. **Example:** 'After 300 meters turn right onto Wall Street.'.

<span class="name">ssml</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-navigation-notificationformatoption">NotificationFormatOption</a></span>  
Phoneme in SSML format is included in the notification, only if <a href="sdk-for-flutter-navigate-navigation-maneuvernotificationoptions-enablephoneme">ManeuverNotificationOptions.enablePhoneme</a> option is set to `true`. **Example:** '<speak>After 300 meters turn right onto `<lang xml:lang="ENG"> <phoneme alphabet="nts" ph="&quot;wɔːl&quot;striːt" orthmode="ignorepunct">Wall Street</phoneme></lang>`. </speak>'. Some 3rd party TTS engines may support it. Please check <a href="https://www.w3.org/TR/speech-synthesis11/">www.w3.org/TR/speech-synthesis11/</a> for detailed information about the SSML format.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-notificationformatoption-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-notificationformatoption-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-notificationformatoption-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-notificationformatoption-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-notificationformatoption-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-notificationformatoption-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-navigation-notificationformatoption-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-notificationformatoption">NotificationFormatOption</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
