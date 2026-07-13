---
title: "EVChargingTariffElementCondition class - search library - Dart API"
slug: "sdk-for-flutter-navigate-search-evchargingtariffelementcondition-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EVChargingTariffElementCondition-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/EVChargingTariffElementCondition-class-sidebar.html">

<div>

# <span class="kind-class">EVChargingTariffElementCondition</span> class

</div>

<div class="section desc markdown">

Condition that the charging session needs to meet to apply the tariff element.

Tariff elements may include conditions that define when they apply:

- Time of day (e.g., 22:00–06:00)
- Day of week (e.g., weekends only)
- Date range (e.g., seasonal pricing)
- Charging session duration
- Battery level thresholds (e.g., overstay fees)

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingtariffelementcondition-evchargingtariffelementcondition">EVChargingTariffElementCondition</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingtariffelementcondition-date">date</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-search-daterange-class">DateRange</a>?</span>  
Date range when the tariff element is valid. This is typically used to indicate seasonal tariffs or to announce an update to the tariff in advance. It may also be used to indicate spot prices, together with time period.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingtariffelementcondition-days">days</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-search-dayofweek">DayOfWeek</a></span>\></span></span>  
Day(s) of the week when the tariff element is valid. An example would be to specify lower prices for weekends

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingtariffelementcondition-duration">duration</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-search-evchargingdurationrange-class">EVChargingDurationRange</a>?</span>  
Duration of the charging session when the tariff element is valid, in seconds.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingtariffelementcondition-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingtariffelementcondition-overstaybatterylevel">overstayBatteryLevel</a></span> <span class="signature">↔ int?</span>  
Minimum battery level when the tariff element is valid, in percentages. This can be used to set additional fees for charging a full or nearly full battery.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingtariffelementcondition-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingtariffelementcondition-time">time</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-search-timeofdayrange-class">TimeOfDayRange</a>?</span>  
Time period when the tariff element is valid, in local time. The time period wraps around to the next day, when end time of the period <a href="sdk-for-flutter-navigate-search-timeofdayrange-to">TimeOfDayRange.to</a> is smaller than the beginning <a href="sdk-for-flutter-navigate-search-timeofdayrange-from">TimeOfDayRange.from</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingtariffelementcondition-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingtariffelementcondition-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-search-evchargingtariffelementcondition-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
