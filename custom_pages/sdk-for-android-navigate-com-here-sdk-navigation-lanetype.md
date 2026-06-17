---
title: "LaneType (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-lanetype"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- LaneType.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.navigation.LaneType</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">LaneType</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>A class that provides information on the available lane properties.
 The lane type values can be combined as follows:
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
</ul></p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">

<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#isAcceleration">isAcceleration</a></code></div>
<div class="col-last even-row-color">
<div class="block">An acceleration lane is a lane, typically on the right side of a roadway, that lets a vehicle
 increase its speed to where it can safely merge with ongoing traffic.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#isAuxiliary">isAuxiliary</a></code></div>
<div class="col-last odd-row-color">
<div class="block">An auxiliary lane is a lane that runs parallel to a motorway and connects the entrance
 ramp/acceleration lane from one interchange exit ramp/deceleration lane of the next
 interchange.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#isBicycle">isBicycle</a></code></div>
<div class="col-last even-row-color">
<div class="block">Bicycle lanes are lanes added to the road bed that only allow bicycle travel as indicated by
 lane markings, signs, buffers or barriers.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#isCenterTurn">isCenterTurn</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Center turn lane is a bidirectional turn lane located in the middle of a road that allows
 traffic in both directions to turn left (right for left side driving countries).</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#isDeceleration">isDeceleration</a></code></div>
<div class="col-last even-row-color">
<div class="block">A deceleration lane is the same as an acceleration lane but used for the opposite scenario.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#isExpress">isExpress</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Express lane is a lane or set of lanes usually physically separated from the major roadway
 with limited entry and exit points to quickly move traffic in and out of a major metropolitan
 city.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#isHighOccupancyVehicle">isHighOccupancyVehicle</a></code></div>
<div class="col-last even-row-color">
<div class="block">A lane which is restricted for high occupancy vehicles.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#isParking">isParking</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Parking lanes are portions of the road bed that may be used for parking legally.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#isPassing">isPassing</a></code></div>
<div class="col-last even-row-color">
<div class="block">A passing lane is a lane that can occur on steep mountain grades or other roads where
 overtaking needs to be regulated for safety (i.e., curvy roads).</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#isRegular">isRegular</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Regular lane is a lane that does not have a specific use.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#isRegulatedAccess">isRegulatedAccess</a></code></div>
<div class="col-last even-row-color">
<div class="block">A regulated lane access is a lane designated as a holding zone, used to regulate traffic
 using time intervals.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#isReversible">isReversible</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A lane in which traffic may travel in either direction, depending on certain conditions
 such as the time of the day to improve traffic flow during rush hours.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#isShoulder">isShoulder</a></code></div>
<div class="col-last even-row-color">
<div class="block">A shoulder lane is a reserved paved area on the side of the road (one or both sides) that is
 not generally used for driving, although it is possible under certain circumstances.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#isSlow">isSlow</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A slow lane, also known as truck (US) or crawler lane (UK), is a lane on long and/or steep
 uphill/downhill stretches of high-speed roads that is designated to facilitate slow traffic.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#isTruckParking">isTruckParking</a></code></div>
<div class="col-last even-row-color">
<div class="block">Truck parking lanes is a wide shoulder lane that may be used for truck parking as well as for
 emergency.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#isTurn">isTurn</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Turn lane is a dedicated lane that is used for making a turn in order not to disrupt ongoing
 traffic.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#isVariableDriving">isVariableDriving</a></code></div>
<div class="col-last even-row-color">
<div class="block">Variable driving lanes are lanes added to a road that open and close to accommodate traffic
 volume and flow using variable indicators.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">LaneType</a><wbr/>(boolean isRegular,
 boolean isHighOccupancyVehicle,
 boolean isReversible,
 boolean isExpress,
 boolean isAcceleration,
 boolean isDeceleration,
 boolean isAuxiliary,
 boolean isSlow,
 boolean isPassing,
 boolean isShoulder,
 boolean isRegulatedAccess,
 boolean isTurn,
 boolean isCenterTurn,
 boolean isTruckParking,
 boolean isParking,
 boolean isVariableDriving,
 boolean isBicycle)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#hashCode()">hashCode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">

<ul class="member-list">
<li>
<section class="detail" id="isRegular">
<h3>isRegular</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRegular</span></div>
<div class="block"><p>Regular lane is a lane that does not have a specific use.</p></div>
</section>
</li>
<li>
<section class="detail" id="isHighOccupancyVehicle">
<h3>isHighOccupancyVehicle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isHighOccupancyVehicle</span></div>
<div class="block"><p>A lane which is restricted for high occupancy vehicles.
 Note: High occupancy vehicles are vehicles with a driver and one or more passengers.</p></div>
</section>
</li>
<li>
<section class="detail" id="isReversible">
<h3>isReversible</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isReversible</span></div>
<div class="block"><p>A lane in which traffic may travel in either direction, depending on certain conditions
 such as the time of the day to improve traffic flow during rush hours.</p></div>
</section>
</li>
<li>
<section class="detail" id="isExpress">
<h3>isExpress</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isExpress</span></div>
<div class="block"><p>Express lane is a lane or set of lanes usually physically separated from the major roadway
 with limited entry and exit points to quickly move traffic in and out of a major metropolitan
 city. An express lane can be reversible, bidirectional, or one-way.</p></div>
</section>
</li>
<li>
<section class="detail" id="isAcceleration">
<h3>isAcceleration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAcceleration</span></div>
<div class="block"><p>An acceleration lane is a lane, typically on the right side of a roadway, that lets a vehicle
 increase its speed to where it can safely merge with ongoing traffic. These lanes can be
 accessed from ramps, rest areas, or weigh stations.</p></div>
</section>
</li>
<li>
<section class="detail" id="isDeceleration">
<h3>isDeceleration</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDeceleration</span></div>
<div class="block"><p>A deceleration lane is the same as an acceleration lane but used for the opposite scenario.</p></div>
</section>
</li>
<li>
<section class="detail" id="isAuxiliary">
<h3>isAuxiliary</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isAuxiliary</span></div>
<div class="block"><p>An auxiliary lane is a lane that runs parallel to a motorway and connects the entrance
 ramp/acceleration lane from one interchange exit ramp/deceleration lane of the next
 interchange.</p></div>
</section>
</li>
<li>
<section class="detail" id="isSlow">
<h3>isSlow</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isSlow</span></div>
<div class="block"><p>A slow lane, also known as truck (US) or crawler lane (UK), is a lane on long and/or steep
 uphill/downhill stretches of high-speed roads that is designated to facilitate slow traffic.</p></div>
</section>
</li>
<li>
<section class="detail" id="isPassing">
<h3>isPassing</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isPassing</span></div>
<div class="block"><p>A passing lane is a lane that can occur on steep mountain grades or other roads where
 overtaking needs to be regulated for safety (i.e., curvy roads). They are used to safely pass
 slow moving vehicles.</p></div>
</section>
</li>
<li>
<section class="detail" id="isShoulder">
<h3>isShoulder</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isShoulder</span></div>
<div class="block"><p>A shoulder lane is a reserved paved area on the side of the road (one or both sides) that is
 not generally used for driving, although it is possible under certain circumstances.</p></div>
</section>
</li>
<li>
<section class="detail" id="isRegulatedAccess">
<h3>isRegulatedAccess</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRegulatedAccess</span></div>
<div class="block"><p>A regulated lane access is a lane designated as a holding zone, used to regulate traffic
 using time intervals. Regulated lane access is only coded for truck holding zones that are
 used to regulate truck access into tunnels and over bridges using time intervals (e.g., some
 tunnel accesses in Switzerland).</p></div>
</section>
</li>
<li>
<section class="detail" id="isTurn">
<h3>isTurn</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTurn</span></div>
<div class="block"><p>Turn lane is a dedicated lane that is used for making a turn in order not to disrupt ongoing
 traffic.</p></div>
</section>
</li>
<li>
<section class="detail" id="isCenterTurn">
<h3>isCenterTurn</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCenterTurn</span></div>
<div class="block"><p>Center turn lane is a bidirectional turn lane located in the middle of a road that allows
 traffic in both directions to turn left (right for left side driving countries).</p></div>
</section>
</li>
<li>
<section class="detail" id="isTruckParking">
<h3>isTruckParking</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTruckParking</span></div>
<div class="block"><p>Truck parking lanes is a wide shoulder lane that may be used for truck parking as well as for
 emergency.</p></div>
</section>
</li>
<li>
<section class="detail" id="isParking">
<h3>isParking</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isParking</span></div>
<div class="block"><p>Parking lanes are portions of the road bed that may be used for parking legally. They may
 allow vehicles to use them as driving lanes at times, though.</p></div>
</section>
</li>
<li>
<section class="detail" id="isVariableDriving">
<h3>isVariableDriving</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isVariableDriving</span></div>
<div class="block"><p>Variable driving lanes are lanes added to a road that open and close to accommodate traffic
 volume and flow using variable indicators.</p></div>
</section>
</li>
<li>
<section class="detail" id="isBicycle">
<h3>isBicycle</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isBicycle</span></div>
<div class="block"><p>Bicycle lanes are lanes added to the road bed that only allow bicycle travel as indicated by
 lane markings, signs, buffers or barriers.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean,boolean)">
<h3>LaneType</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">LaneType</span><wbr/><span class="parameters">(boolean isRegular,
 boolean isHighOccupancyVehicle,
 boolean isReversible,
 boolean isExpress,
 boolean isAcceleration,
 boolean isDeceleration,
 boolean isAuxiliary,
 boolean isSlow,
 boolean isPassing,
 boolean isShoulder,
 boolean isRegulatedAccess,
 boolean isTurn,
 boolean isCenterTurn,
 boolean isTruckParking,
 boolean isParking,
 boolean isVariableDriving,
 boolean isBicycle)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>isRegular</code> - <p>Regular lane is a lane that does not have a specific use.</p></dd>
<dd><code>isHighOccupancyVehicle</code> - <p>A lane which is restricted for high occupancy vehicles.
 Note: High occupancy vehicles are vehicles with a driver and one or more passengers.</p></dd>
<dd><code>isReversible</code> - <p>A lane in which traffic may travel in either direction, depending on certain conditions
 such as the time of the day to improve traffic flow during rush hours.</p></dd>
<dd><code>isExpress</code> - <p>Express lane is a lane or set of lanes usually physically separated from the major roadway
 with limited entry and exit points to quickly move traffic in and out of a major metropolitan
 city. An express lane can be reversible, bidirectional, or one-way.</p></dd>
<dd><code>isAcceleration</code> - <p>An acceleration lane is a lane, typically on the right side of a roadway, that lets a vehicle
 increase its speed to where it can safely merge with ongoing traffic. These lanes can be
 accessed from ramps, rest areas, or weigh stations.</p></dd>
<dd><code>isDeceleration</code> - <p>A deceleration lane is the same as an acceleration lane but used for the opposite scenario.</p></dd>
<dd><code>isAuxiliary</code> - <p>An auxiliary lane is a lane that runs parallel to a motorway and connects the entrance
 ramp/acceleration lane from one interchange exit ramp/deceleration lane of the next
 interchange.</p></dd>
<dd><code>isSlow</code> - <p>A slow lane, also known as truck (US) or crawler lane (UK), is a lane on long and/or steep
 uphill/downhill stretches of high-speed roads that is designated to facilitate slow traffic.</p></dd>
<dd><code>isPassing</code> - <p>A passing lane is a lane that can occur on steep mountain grades or other roads where
 overtaking needs to be regulated for safety (i.e., curvy roads). They are used to safely pass
 slow moving vehicles.</p></dd>
<dd><code>isShoulder</code> - <p>A shoulder lane is a reserved paved area on the side of the road (one or both sides) that is
 not generally used for driving, although it is possible under certain circumstances.</p></dd>
<dd><code>isRegulatedAccess</code> - <p>A regulated lane access is a lane designated as a holding zone, used to regulate traffic
 using time intervals. Regulated lane access is only coded for truck holding zones that are
 used to regulate truck access into tunnels and over bridges using time intervals (e.g., some
 tunnel accesses in Switzerland).</p></dd>
<dd><code>isTurn</code> - <p>Turn lane is a dedicated lane that is used for making a turn in order not to disrupt ongoing
 traffic.</p></dd>
<dd><code>isCenterTurn</code> - <p>Center turn lane is a bidirectional turn lane located in the middle of a road that allows
 traffic in both directions to turn left (right for left side driving countries).</p></dd>
<dd><code>isTruckParking</code> - <p>Truck parking lanes is a wide shoulder lane that may be used for truck parking as well as for
 emergency.</p></dd>
<dd><code>isParking</code> - <p>Parking lanes are portions of the road bed that may be used for parking legally. They may
 allow vehicles to use them as driving lanes at times, though.</p></dd>
<dd><code>isVariableDriving</code> - <p>Variable driving lanes are lanes added to a road that open and close to accommodate traffic
 volume and flow using variable indicators.</p></dd>
<dd><code>isBicycle</code> - <p>Bicycle lanes are lanes added to the road bed that only allow bicycle travel as indicated by
 lane markings, signs, buffers or barriers.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>





</div>
`
}</HTMLBlock>
