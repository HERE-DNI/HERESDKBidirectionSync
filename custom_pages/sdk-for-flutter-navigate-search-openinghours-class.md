---
title: "OpeningHours class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-openinghours-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/OpeningHours-class-sidebar.html">

<div>

# <span class="kind-class">OpeningHours</span> class

</div>

<div class="section desc markdown">

Represents opening hours information.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-search-openinghours-openinghours">OpeningHours</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-text" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span> <span class="parameter-name">text</span>, </span><span id="sdk-for-flutter-navigate-param-isOpen" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">isOpen</span>, </span><span id="sdk-for-flutter-navigate-param-scheduleDetailsList" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-scheduledetails-class">ScheduleDetails</a></span>\></span></span> <span class="parameter-name">scheduleDetailsList</span>, </span><span id="sdk-for-flutter-navigate-param-categories" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-placecategory-class">PlaceCategory</a></span>\></span></span> <span class="parameter-name">categories</span></span>)</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-search-openinghours-categories">categories</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-placecategory-class">PlaceCategory</a></span>\></span></span>  
The list of categories related to opening hours information. This data is not available in offline search.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-openinghours-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-openinghours-isopen">isOpen</a></span> <span class="signature">↔ bool</span>  
Boolean flag informing if the place is open or closed at the time when the search request was initiated. For offline search, this is calculated using device's time, so it may give incorrect value if device and place are located in different time zones.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-openinghours-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-openinghours-scheduledetailslist">scheduleDetailsList</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-scheduledetails-class">ScheduleDetails</a></span>\></span></span>  
The list of schedule details.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-openinghours-text">text</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter">String</span>\></span></span>  
The list of opening hours presented as localized text.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-search-openinghours-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-openinghours-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-search-openinghours-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

