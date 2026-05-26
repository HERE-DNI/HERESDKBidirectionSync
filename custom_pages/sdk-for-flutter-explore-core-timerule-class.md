---
title: "TimeRule class abstract"
slug: "sdk-for-flutter-explore-core-timerule-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TimeRule-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core/TimeRule-class.html#constructors">Constructors</a></li>
<li><a href="core/TimeRule/TimeRule.html">TimeRule</a></li>
<li class="section-title">
<a href="core/TimeRule-class.html#instance-properties">Properties</a>
</li>
<li><a href="core/TimeRule/dstSpec.html">dstSpec</a></li>
<li class="inherited"><a href="core/TimeRule/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="core/TimeRule/runtimeType.html">runtimeType</a></li>
<li><a href="core/TimeRule/timeRuleString.html">timeRuleString</a></li>
<li><a href="core/TimeRule/timeZoneOffsetSeconds.html">timeZoneOffsetSeconds</a></li>
<li class="section-title"><a href="core/TimeRule-class.html#instance-methods">Methods</a></li>
<li><a href="core/TimeRule/appliesTo.html">appliesTo</a></li>
<li class="inherited"><a href="core/TimeRule/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core/TimeRule/toString.html">toString</a></li>
<li class="section-title inherited"><a href="core/TimeRule-class.html#operators">Operators</a></li>
<li class="inherited"><a href="core/TimeRule/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-core-library</li>
<li class="self-crumb">TimeRule class</li>
</ol>
<div class="self-name">TimeRule</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="core/TimeRule-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TimeRule class abstract</h1></div>
<section class="desc markdown">
<p>Used to indicate a time period of one or more intervals in <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/concepts/time-domain.html">GDF</a> specification.</p>
<p>For example:
-*(M3f21h2){M9}(M11f12h2){-M9}+(h15){h2}(h20){h2}, which represents:
March 2nd Sunday 02h:00m for 9 months
ONLY DURING November 1st Sunday 02h:00m from 9 months ago
BUT NOT from 15:00 to 17:00 OR 20:00 to 22:00</p>
<p>The operator * represents reccuring occurrence, <code>+</code> represents a logical OR operation and <code>-</code> represents exclusion meaning, BUT NOT operations.</p>
<p>This example string represents a time period that meets the following criteria:</p>
<ul>
<li><code>M3f21h2</code>: M3 denotes third month of the year, i.e. March,
f2 stands for the second Sunday of the month (as "f" might indicate "first", "second", "third", etc.),
1 stands for the day of the week (1...7, Day of week, Sunday = day 1), and h2 represents the hour of the day (02:00) in 24 hour format.</li>
<li><code>{M9}</code>: This denotes "for 9 months", with "M9" standing for nine months. The brackets {} indicate a duration.</li>
<li><code>M11f12h2</code>: M11 denotes 11th month of the year, i.e. November, f1 stands for the first Monday of the month,
2 stands for the day of the week (1...7, Day of week, Monday = day 2), and h2 represents the hour of the day (02:00) in 24 hour format.</li>
<li>{-M9}: This denotes "9 months ago from the current stated time", with "-M9" standing for nine months in the past.</li>
<li><code>(h15){h2}(h20){h2}</code>: 15:00 to 17:00 OR 20:00 to 22:00
The brackets {} denotes duration, and the negative sign - represents a past duration.</li>
</ul>
<p>Note: The time period is a logical AND (&amp;&amp;) combination of two components or points in time and it only applies if a point in time is in both components.</p>
<p>For more advanced examples of <code>TimeRule</code> see <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html#time-domain-advanced-examples">here</a>.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TimeRule">
/sdk-for-flutter-explore-core-timerule-timerule(String timeRule, int timeZoneOffsetSeconds, String dstSpec)
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="dstSpec">
/sdk-for-flutter-explore-core-timerule-dstspec
→ String
</dt>
<dd>
  Day saving time specification, as a string in ISO 14825 format, for the location where the time rule applies.
Gets the value of day saving time specification, as a string in ISO 14825 format, for the location where the time rule applies.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-core-timerule-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-core-timerule-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="timeRuleString">
/sdk-for-flutter-explore-core-timerule-timerulestring
→ String
</dt>
<dd>
  The time rule as a string in ISO 14825 format.
Gets the value of time rule as a string in ISO 14825 format.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="timeZoneOffsetSeconds">
/sdk-for-flutter-explore-core-timerule-timezoneoffsetseconds
→ int
</dt>
<dd>
  The time zone offset in seconds for the location where the time rule applies.
Gets the value of time zone offset in seconds for the location where the time rule applies.
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="appliesTo">
/sdk-for-flutter-explore-core-timerule-appliesto(<wbr/>DateTime dateTime)
    → bool

</dt>
<dd>
<li><code>dateTime</code> date and time that should be used for rule verification.</li>
</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-core-timerule-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-core-timerule-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-explore-core-timerule-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-core-core-library</li>
<li class="self-crumb">TimeRule class</li>
</ol>
<h5>core library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
`
}</HTMLBlock>
