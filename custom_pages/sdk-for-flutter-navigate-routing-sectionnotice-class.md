---
title: "SectionNotice class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-sectionnotice-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/SectionNotice-class-sidebar.html">

<div>

# <span class="kind-class">SectionNotice</span> class

</div>

<div class="section desc markdown">

Explains an issue encountered in a <a href="sdk-for-flutter-navigate-routing-section-class">Section</a>.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-routing-sectionnotice-sectionnotice">SectionNotice</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-code" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span> <span class="parameter-name">code</span>, </span><span id="sdk-for-flutter-navigate-param-severity" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity</a></span> <span class="parameter-name">severity</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-routing-sectionnotice-code">code</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode</a></span>  
The notice code.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-sectionnotice-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-sectionnotice-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-sectionnotice-severity">severity</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-noticeseverity">NoticeSeverity</a></span>  
The notice severity.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-sectionnotice-violatedrestrictions">violatedRestrictions</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-violatedrestriction-class">ViolatedRestriction</a></span>\></span></span>  
The following property `violated_restrictions` contains the notice detail information. Only three types of restrictions can have notice details: time dependent restriction, vehicle restriction and transport mode restriction. There is no one-to-one match of the `SectionNotice.code` and these three restriction types. For example, if `SectionNotice.code` is <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode.violatedVehicleRestriction</a>, then it can be either vehicle restriction or transport mode restriction. If `SectionNotice.code` is <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode.seasonalClosure</a>, then it is time dependent restriction. If the section notice is none of the above-mentioned three types, then this will be an empty list.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-sectionnotice-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-sectionnotice-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-routing-sectionnotice-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

