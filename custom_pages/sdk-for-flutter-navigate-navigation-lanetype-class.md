---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-lanetype-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LaneType-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">LaneType class</li>
</ol>
<div class="self-name">LaneType</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/LaneType-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>LaneType class</h1></div>
<section class="desc markdown">
<p>A class that provides information on the available lane properties.</p>
<p>The lane type values can be combined as follows:</p>
<ul>
<li>High Occupancy Vehicle, Reversible</li>
<li>High Occupancy Vehicle and Express</li>
<li>Reversible and Express</li>
<li>High Occupancy Vehicle, Reversible and Express</li>
<li>High Occupancy Vehicle and Acceleration</li>
<li>Reversible, Acceleration Lane</li>
<li>High Occupancy Vehicle, Reversible, Acceleration Lane</li>
<li>Express and Acceleration</li>
<li>High Occupancy Vehicle and Deceleration</li>
<li>Reversible, Deceleration Lane</li>
<li>High Occupancy Vehicle, Reversible, Deceleration Lane</li>
<li>Express and Deceleration</li>
</ul>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="LaneType">
/sdk-for-flutter-navigate-navigation-lanetype-lanetype(bool isRegular, bool isHighOccupancyVehicle, bool isReversible, bool isExpress, bool isAcceleration, bool isDeceleration, bool isAuxiliary, bool isSlow, bool isPassing, bool isShoulder, bool isRegulatedAccess, bool isTurn, bool isCenterTurn, bool isTruckParking, bool isParking, bool isVariableDriving, bool isBicycle)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-lanetype-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="isAcceleration">
/sdk-for-flutter-navigate-navigation-lanetype-isacceleration
↔ bool
</dt>
<dd>
  An acceleration lane is a lane, typically on the right side of a roadway, that lets a vehicle
increase its speed to where it can safely merge with ongoing traffic. These lanes can be
accessed from ramps, rest areas, or weigh stations.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isAuxiliary">
/sdk-for-flutter-navigate-navigation-lanetype-isauxiliary
↔ bool
</dt>
<dd>
  An auxiliary lane is a lane that runs parallel to a motorway and connects the entrance
ramp/acceleration lane from one interchange exit ramp/deceleration lane of the next
interchange.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isBicycle">
/sdk-for-flutter-navigate-navigation-lanetype-isbicycle
↔ bool
</dt>
<dd>
  Bicycle lanes are lanes added to the road bed that only allow bicycle travel as indicated by
lane markings, signs, buffers or barriers.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isCenterTurn">
/sdk-for-flutter-navigate-navigation-lanetype-iscenterturn
↔ bool
</dt>
<dd>
  Center turn lane is a bidirectional turn lane located in the middle of a road that allows
traffic in both directions to turn left (right for left side driving countries).
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isDeceleration">
/sdk-for-flutter-navigate-navigation-lanetype-isdeceleration
↔ bool
</dt>
<dd>
  A deceleration lane is the same as an acceleration lane but used for the opposite scenario.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isExpress">
/sdk-for-flutter-navigate-navigation-lanetype-isexpress
↔ bool
</dt>
<dd>
  Express lane is a lane or set of lanes usually physically separated from the major roadway
with limited entry and exit points to quickly move traffic in and out of a major metropolitan
city. An express lane can be reversible, bidirectional, or one-way.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isHighOccupancyVehicle">
/sdk-for-flutter-navigate-navigation-lanetype-ishighoccupancyvehicle
↔ bool
</dt>
<dd>
  A lane which is restricted for high occupancy vehicles.
Note: High occupancy vehicles are vehicles with a driver and one or more passengers.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isParking">
/sdk-for-flutter-navigate-navigation-lanetype-isparking
↔ bool
</dt>
<dd>
  Parking lanes are portions of the road bed that may be used for parking legally. They may
allow vehicles to use them as driving lanes at times, though.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isPassing">
/sdk-for-flutter-navigate-navigation-lanetype-ispassing
↔ bool
</dt>
<dd>
  A passing lane is a lane that can occur on steep mountain grades or other roads where
overtaking needs to be regulated for safety (i.e., curvy roads). They are used to safely pass
slow moving vehicles.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isRegular">
/sdk-for-flutter-navigate-navigation-lanetype-isregular
↔ bool
</dt>
<dd>
  Regular lane is a lane that does not have a specific use.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isRegulatedAccess">
/sdk-for-flutter-navigate-navigation-lanetype-isregulatedaccess
↔ bool
</dt>
<dd>
  A regulated lane access is a lane designated as a holding zone, used to regulate traffic
using time intervals. Regulated lane access is only coded for truck holding zones that are
used to regulate truck access into tunnels and over bridges using time intervals (e.g., some
tunnel accesses in Switzerland).
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isReversible">
/sdk-for-flutter-navigate-navigation-lanetype-isreversible
↔ bool
</dt>
<dd>
  A lane in which traffic may travel in either direction, depending on certain conditions
such as the time of the day to improve traffic flow during rush hours.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isShoulder">
/sdk-for-flutter-navigate-navigation-lanetype-isshoulder
↔ bool
</dt>
<dd>
  A shoulder lane is a reserved paved area on the side of the road (one or both sides) that is
not generally used for driving, although it is possible under certain circumstances.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isSlow">
/sdk-for-flutter-navigate-navigation-lanetype-isslow
↔ bool
</dt>
<dd>
  A slow lane, also known as truck (US) or crawler lane (UK), is a lane on long and/or steep
uphill/downhill stretches of high-speed roads that is designated to facilitate slow traffic.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isTruckParking">
/sdk-for-flutter-navigate-navigation-lanetype-istruckparking
↔ bool
</dt>
<dd>
  Truck parking lanes is a wide shoulder lane that may be used for truck parking as well as for
emergency.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isTurn">
/sdk-for-flutter-navigate-navigation-lanetype-isturn
↔ bool
</dt>
<dd>
  Turn lane is a dedicated lane that is used for making a turn in order not to disrupt ongoing
traffic.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isVariableDriving">
/sdk-for-flutter-navigate-navigation-lanetype-isvariabledriving
↔ bool
</dt>
<dd>
  Variable driving lanes are lanes added to a road that open and close to accommodate traffic
volume and flow using variable indicators.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-lanetype-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-lanetype-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-lanetype-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-lanetype-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

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
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">LaneType class</li>
</ol>
<h5>navigation library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>
