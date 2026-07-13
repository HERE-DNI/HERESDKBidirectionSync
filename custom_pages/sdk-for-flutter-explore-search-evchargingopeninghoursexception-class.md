---
title: "EVChargingOpeningHoursException class - search library - Dart API"
slug: "sdk-for-flutter-explore-search-evchargingopeninghoursexception-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/EVChargingOpeningHoursException-class-sidebar.html">

<div>

# <span class="kind-class">EVChargingOpeningHoursException</span> class

</div>

<div class="section desc markdown">

Represents exceptions to the regular opening hours schedule for EV charging locations, such as special closures or extended hours.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingopeninghoursexception-evchargingopeninghoursexception">EVChargingOpeningHoursException</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingopeninghoursexception-closed">closed</a></span> <span class="signature">↔ bool</span>  
True if the charging location is closed on particular date, in which case <a href="sdk-for-flutter-explore-search-evchargingopeninghoursexception-periods">EVChargingOpeningHoursException.periods</a> is empty.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingopeninghoursexception-date">date</a></span> <span class="signature">↔ DateTime</span>  
Date of special opening hours.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingopeninghoursexception-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingopeninghoursexception-periods">periods</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-search-timeofdayrange-class">TimeOfDayRange</a></span>\></span></span>  
A list of time periods when the charging location is open on the specified date. The time periods are in the local time zone of the charging location, and are represented as a list of objects with <a href="sdk-for-flutter-explore-search-timeofdayrange-from">TimeOfDayRange.from</a> and <a href="sdk-for-flutter-explore-search-timeofdayrange-to">TimeOfDayRange.to</a> properties.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingopeninghoursexception-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingopeninghoursexception-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingopeninghoursexception-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-search-evchargingopeninghoursexception-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

