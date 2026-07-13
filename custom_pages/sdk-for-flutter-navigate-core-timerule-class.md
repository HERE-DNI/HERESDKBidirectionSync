---
title: "TimeRule class - core library - Dart API"
slug: "sdk-for-flutter-navigate-core-timerule-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="core/TimeRule-class-sidebar.html">

<div>

# <span class="kind-class">TimeRule</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Used to indicate a time period of one or more intervals in <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/concepts/time-domain.html">GDF</a> specification.

For example: -\*(M3f21h2){M9}(M11f12h2){-M9}+(h15){h2}(h20){h2}, which represents: March 2nd Sunday 02h:00m for 9 months ONLY DURING November 1st Sunday 02h:00m from 9 months ago BUT NOT from 15:00 to 17:00 OR 20:00 to 22:00

The operator \* represents reccuring occurrence, `+` represents a logical OR operation and `-` represents exclusion meaning, BUT NOT operations.

This example string represents a time period that meets the following criteria:

- `M3f21h2`: M3 denotes third month of the year, i.e. March, f2 stands for the second Sunday of the month (as "f" might indicate "first", "second", "third", etc.), 1 stands for the day of the week (1...7, Day of week, Sunday = day 1), and h2 represents the hour of the day (02:00) in 24 hour format.

- `{M9}`: This denotes "for 9 months", with "M9" standing for nine months. The brackets {} indicate a duration.

- `M11f12h2`: M11 denotes 11th month of the year, i.e. November, f1 stands for the first Monday of the month, 2 stands for the day of the week (1...7, Day of week, Monday = day 2), and h2 represents the hour of the day (02:00) in 24 hour format.

- {-M9}: This denotes "9 months ago from the current stated time", with "-M9" standing for nine months in the past.

-     (h15){h2}(h20){h2}

  : 15:00 to 17:00 OR 20:00 to 22:00 The brackets {} denotes duration, and the negative sign - represents a past duration.

Note: The time period is a logical AND (&&) combination of two components or points in time and it only applies if a point in time is in both components.

For more advanced examples of `TimeRule` see <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html#time-domain-advanced-examples">here</a>.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-core-timerule-timerule">TimeRule</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-timeRule" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">timeRule</span>, </span><span id="sdk-for-flutter-navigate-param-timeZoneOffsetSeconds" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">timeZoneOffsetSeconds</span>, </span><span id="sdk-for-flutter-navigate-param-dstSpec" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">dstSpec</span></span>)</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-core-timerule-dstspec">dstSpec</a></span> <span class="signature">→ String</span>  
Day saving time specification, as a string in ISO 14825 format, for the location where the time rule applies. Gets the value of day saving time specification, as a string in ISO 14825 format, for the location where the time rule applies.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-timerule-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-timerule-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-timerule-timerulestring">timeRuleString</a></span> <span class="signature">→ String</span>  
The time rule as a string in ISO 14825 format. Gets the value of time rule as a string in ISO 14825 format.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-timerule-timezoneoffsetseconds">timeZoneOffsetSeconds</a></span> <span class="signature">→ int</span>  
The time zone offset in seconds for the location where the time rule applies. Gets the value of time zone offset in seconds for the location where the time rule applies.

<div class="features">

<span class="feature">no setter</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-core-timerule-appliesto">appliesTo</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-appliesTo-param-dateTime" class="parameter"><span class="type-annotation">DateTime</span> <span class="parameter-name">dateTime</span></span>) <span class="returntype parameter">→ bool</span> </span>  
<li>

`dateTime` date and time that should be used for rule verification.

</li>

<span class="name"><a href="sdk-for-flutter-navigate-core-timerule-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-core-timerule-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-core-timerule-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

