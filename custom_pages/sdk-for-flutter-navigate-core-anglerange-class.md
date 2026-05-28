---
title: "AngleRange class"
slug: "sdk-for-flutter-navigate-core-anglerange-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- AngleRange-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="core/AngleRange-class.html#constructors">Constructors</a></li>
<li><a href="core/AngleRange/AngleRange.html">AngleRange</a></li>
<li><a href="core/AngleRange/AngleRange.fullCircle.html">fullCircle</a></li>
<li class="section-title">
<a href="core/AngleRange-class.html#instance-properties">Properties</a>
</li>
<li><a href="core/AngleRange/extent.html">extent</a></li>
<li><a href="core/AngleRange/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="core/AngleRange/runtimeType.html">runtimeType</a></li>
<li><a href="core/AngleRange/start.html">start</a></li>
<li class="section-title"><a href="core/AngleRange-class.html#instance-methods">Methods</a></li>
<li><a href="core/AngleRange/closestInRange.html">closestInRange</a></li>
<li><a href="core/AngleRange/inRange.html">inRange</a></li>
<li><a href="core/AngleRange/max.html">max</a></li>
<li class="inherited"><a href="core/AngleRange/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="core/AngleRange/toString.html">toString</a></li>
<li class="section-title"><a href="core/AngleRange-class.html#operators">Operators</a></li>
<li><a href="core/AngleRange/operator_equals.html">operator ==</a></li>
<li class="section-title"><a href="core/AngleRange-class.html#static-methods">Static methods</a></li>
<li><a href="core/AngleRange/fromDirectionDegreesClockwise.html">fromDirectionDegreesClockwise</a></li>
<li><a href="core/AngleRange/fromMinMaxDegreesClockwise.html">fromMinMaxDegreesClockwise</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-core-core-library</li>
<li class="self-crumb">AngleRange class</li>
</ol>
<div class="self-name">AngleRange</div>
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
<div class="main-content" data-above-sidebar="core/core-library-sidebar.html" data-below-sidebar="core/AngleRange-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>AngleRange class</h1></div>
<section class="desc markdown">
<p>Represents angle ranges as a circular sector by using an absolute start angle
and a relative range angle called extent.</p>
<p>They both define a sector on a
circle. All angles are in degrees and are clockwise-oriented.
By default, the AngleRange represents the entire circle, the value is in the range of [0, 360].
Values will be corrected during construction using normalization
for the start angle and clamping for the extent angle, ensuring a valid range
for all possible inputs.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Annotations</dt>
<dd>
<ul class="annotation-list clazz-relationships">
<li>@<a href="https://pub.dev/documentation/meta/1.17.0/meta/immutable-constant.html">immutable</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="AngleRange">
/sdk-for-flutter-navigate-core-anglerange-anglerange(double start, double extent)
</dt>
<dd>
          Constructs an AngleRange from the provided start and extent angles.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="AngleRange.fullCircle">
/sdk-for-flutter-navigate-core-anglerange-anglerange-fullcircle()
</dt>
<dd>
          Constructs a range covering a full circle.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="extent">
/sdk-for-flutter-navigate-core-anglerange-extent
→ double
</dt>
<dd>
  The angle range extent, running clockwise, in degrees from start.
The value is in the range of [0, 360] degrees.
  <div class="features">final</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-core-anglerange-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-core-anglerange-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="start">
/sdk-for-flutter-navigate-core-anglerange-start
→ double
</dt>
<dd>
  Start angle, running clockwise, in degrees from north.
The value is in the range of [0, 360) degrees.
  <div class="features">final</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="closestInRange">
/sdk-for-flutter-navigate-core-anglerange-closestinrange(<wbr/>double angleClockwiseInDegreesFromNorth)
    → double

</dt>
<dd>
  Get the angle that is closest to the given one and in range.
  

</dd>
<dt class="callable" id="inRange">
/sdk-for-flutter-navigate-core-anglerange-inrange(<wbr/>double angleClockwiseInDegreesFromNorth)
    → bool

</dt>
<dd>
  Check if a given angle in degrees, clockwise from north is in range or not.
  

</dd>
<dt class="callable" id="max">
/sdk-for-flutter-navigate-core-anglerange-max(<wbr/>)
    → double

</dt>
<dd>
  Get the maximum angle defined by the range in degrees, clockwise from north,
normalized to [0,360).
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-core-anglerange-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-core-anglerange-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable" id="operator ==">
/sdk-for-flutter-navigate-core-anglerange-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

</dd>
</dl>
</section>
<section class="summary offset-anchor" id="static-methods">
<h2>Static Methods</h2>
<dl class="callables">
<dt class="callable" id="fromDirectionDegreesClockwise">
/sdk-for-flutter-navigate-core-anglerange-fromdirectiondegreesclockwise(<wbr/>double center, double extent)
    → /sdk-for-flutter-navigate-core-anglerange-class

</dt>
<dd>
  Constructs an AngleRange from the provided center angle defining the
direction and an angular width to extent the range by 50% clockwise and
50% counter-clockwise from its center angle.
  

</dd>
<dt class="callable" id="fromMinMaxDegreesClockwise">
/sdk-for-flutter-navigate-core-anglerange-fromminmaxdegreesclockwise(<wbr/>double min, double max)
    → /sdk-for-flutter-navigate-core-anglerange-class

</dt>
<dd>
  Constructs an AngleRange from the provided minimum and maximum angles.
  

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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-core-core-library</li>
<li class="self-crumb">AngleRange class</li>
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
