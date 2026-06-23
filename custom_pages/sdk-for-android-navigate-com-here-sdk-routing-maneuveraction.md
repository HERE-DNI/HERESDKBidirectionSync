---
title: "ManeuverAction (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-maneuveraction"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- ManeuverAction.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a>&gt;
<div class="inheritance">com.here.sdk.routing.ManeuverAction</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>

<div class="type-signature"><span class="modifiers">public enum </span><span class="element-name type-name-label">ManeuverAction</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a>&gt;</span></div>
<div class="block"><p>Maneuver action type.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="inherited-list">

<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">Enum.EnumDesc</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a> extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a>&gt;&gt;</code></div>
</section>
</li>
<!-- =========== ENUM CONSTANT SUMMARY =========== -->
<li>
<section class="constants-summary" id="enum-constant-summary">

<div class="caption"><span>Enum Constants</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Enum Constant</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#ARRIVE">ARRIVE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Arrival maneuver, such as "You have reached your destination/waypoint".</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#CONTINUE_ON">CONTINUE_ON</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Continue maneuver, such as "Continue straight ahead".</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#DEPART">DEPART</a></code></div>
<div class="col-last even-row-color">
<div class="block">Departure maneuver, such as "Head towards".</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#ENTER_HIGHWAY_FROM_LEFT">ENTER_HIGHWAY_FROM_LEFT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Merge onto a highway from the left side.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#ENTER_HIGHWAY_FROM_RIGHT">ENTER_HIGHWAY_FROM_RIGHT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Merge onto a highway from the right side.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#LEFT_EXIT">LEFT_EXIT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Left exit maneuver, such as "Take the exit".</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#LEFT_FORK">LEFT_FORK</a></code></div>
<div class="col-last even-row-color">
<div class="block">Left fork maneuver, such as "Keep left".</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#LEFT_RAMP">LEFT_RAMP</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Left ramp maneuver, such as "Join the highway".</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#LEFT_ROUNDABOUT_ENTER">LEFT_ROUNDABOUT_ENTER</a></code></div>
<div class="col-last even-row-color">
<div class="block">Roundabout maneuver (left-hand traffic), such as "Enter the roundabout".</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#LEFT_ROUNDABOUT_EXIT1">LEFT_ROUNDABOUT_EXIT1</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Roundabout maneuver (left-hand traffic), such as  "Take the first exit at the roundabout".</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#LEFT_ROUNDABOUT_EXIT10">LEFT_ROUNDABOUT_EXIT10</a></code></div>
<div class="col-last even-row-color">
<div class="block">Roundabout maneuver (left-hand traffic), such as "Take the tenth exit at the roundabout".</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#LEFT_ROUNDABOUT_EXIT11">LEFT_ROUNDABOUT_EXIT11</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Roundabout maneuver (left-hand traffic), such as "Take the eleventh exit at the roundabout".</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#LEFT_ROUNDABOUT_EXIT12">LEFT_ROUNDABOUT_EXIT12</a></code></div>
<div class="col-last even-row-color">
<div class="block">Roundabout maneuver (left-hand traffic), such as "Take the twelfth exit at the roundabout".</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#LEFT_ROUNDABOUT_EXIT2">LEFT_ROUNDABOUT_EXIT2</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Roundabout maneuver (left-hand traffic), such as "Take the second exit at the roundabout".</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#LEFT_ROUNDABOUT_EXIT3">LEFT_ROUNDABOUT_EXIT3</a></code></div>
<div class="col-last even-row-color">
<div class="block">Roundabout maneuver (left-hand traffic), such as "Take the third exit at the roundabout".</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#LEFT_ROUNDABOUT_EXIT4">LEFT_ROUNDABOUT_EXIT4</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Roundabout maneuver (left-hand traffic), such as "Take the fourth exit at the roundabout".</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#LEFT_ROUNDABOUT_EXIT5">LEFT_ROUNDABOUT_EXIT5</a></code></div>
<div class="col-last even-row-color">
<div class="block">Roundabout maneuver (left-hand traffic), such as "Take the fifth exit at the roundabout".</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#LEFT_ROUNDABOUT_EXIT6">LEFT_ROUNDABOUT_EXIT6</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Roundabout maneuver (left-hand traffic), such as "Take the sixth exit at the roundabout".</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#LEFT_ROUNDABOUT_EXIT7">LEFT_ROUNDABOUT_EXIT7</a></code></div>
<div class="col-last even-row-color">
<div class="block">Roundabout maneuver (left-hand traffic), such as "Take the seventh exit at the roundabout".</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#LEFT_ROUNDABOUT_EXIT8">LEFT_ROUNDABOUT_EXIT8</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Roundabout maneuver (left-hand traffic), such as "Take the eighth exit at the roundabout".</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#LEFT_ROUNDABOUT_EXIT9">LEFT_ROUNDABOUT_EXIT9</a></code></div>
<div class="col-last even-row-color">
<div class="block">Roundabout maneuver (left-hand traffic), such as "Take the ninth exit at the roundabout".</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#LEFT_ROUNDABOUT_PASS">LEFT_ROUNDABOUT_PASS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Roundabout maneuver (left-hand traffic), such as "Pass the roundabout".</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#LEFT_TURN">LEFT_TURN</a></code></div>
<div class="col-last even-row-color">
<div class="block">Left turn maneuver, such as "Turn left".</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#LEFT_U_TURN">LEFT_U_TURN</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Left-hand U-turn maneuver, such as "Make a U-turn".</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#MIDDLE_FORK">MIDDLE_FORK</a></code></div>
<div class="col-last even-row-color">
<div class="block">Middle fork maneuver, such as "Keep middle".</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#RIGHT_EXIT">RIGHT_EXIT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Right exit maneuver, such as "Take the exit".</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#RIGHT_FORK">RIGHT_FORK</a></code></div>
<div class="col-last even-row-color">
<div class="block">Right fork maneuver, such as "Keep right".</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#RIGHT_RAMP">RIGHT_RAMP</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Right ramp maneuver, such as "Join the highway".</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#RIGHT_ROUNDABOUT_ENTER">RIGHT_ROUNDABOUT_ENTER</a></code></div>
<div class="col-last even-row-color">
<div class="block">Roundabout maneuver (right-hand traffic), such as "Enter the roundabout".</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#RIGHT_ROUNDABOUT_EXIT1">RIGHT_ROUNDABOUT_EXIT1</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Roundabout maneuver (right-hand traffic), such as "Take the first exit at the roundabout".</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#RIGHT_ROUNDABOUT_EXIT10">RIGHT_ROUNDABOUT_EXIT10</a></code></div>
<div class="col-last even-row-color">
<div class="block">Roundabout maneuver (right-hand traffic), such as "Take the tenth exit at the roundabout".</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#RIGHT_ROUNDABOUT_EXIT11">RIGHT_ROUNDABOUT_EXIT11</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Roundabout maneuver (right-hand traffic), such as "Take the eleventh exit at the roundabout".</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#RIGHT_ROUNDABOUT_EXIT12">RIGHT_ROUNDABOUT_EXIT12</a></code></div>
<div class="col-last even-row-color">
<div class="block">Roundabout maneuver (right-hand traffic), such as "Take the twelfth exit at the roundabout".</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#RIGHT_ROUNDABOUT_EXIT2">RIGHT_ROUNDABOUT_EXIT2</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Roundabout maneuver (right-hand traffic), such as "Take the second exit at the roundabout".</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#RIGHT_ROUNDABOUT_EXIT3">RIGHT_ROUNDABOUT_EXIT3</a></code></div>
<div class="col-last even-row-color">
<div class="block">Roundabout maneuver (right-hand traffic), such as "Take the third exit at the roundabout".</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#RIGHT_ROUNDABOUT_EXIT4">RIGHT_ROUNDABOUT_EXIT4</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Roundabout maneuver (right-hand traffic), such as "Take the fourth exit at the roundabout".</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#RIGHT_ROUNDABOUT_EXIT5">RIGHT_ROUNDABOUT_EXIT5</a></code></div>
<div class="col-last even-row-color">
<div class="block">Roundabout maneuver (right-hand traffic), such as "Take the fifth exit at the roundabout".</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#RIGHT_ROUNDABOUT_EXIT6">RIGHT_ROUNDABOUT_EXIT6</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Roundabout maneuver (right-hand traffic), such as "Take the sixth exit at the roundabout".</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#RIGHT_ROUNDABOUT_EXIT7">RIGHT_ROUNDABOUT_EXIT7</a></code></div>
<div class="col-last even-row-color">
<div class="block">Roundabout maneuver (right-hand traffic), such as "Take the seventh exit at the roundabout".</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#RIGHT_ROUNDABOUT_EXIT8">RIGHT_ROUNDABOUT_EXIT8</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Roundabout maneuver (right-hand traffic), such as "Take the eighth exit at the roundabout".</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#RIGHT_ROUNDABOUT_EXIT9">RIGHT_ROUNDABOUT_EXIT9</a></code></div>
<div class="col-last even-row-color">
<div class="block">Roundabout maneuver (right-hand traffic), such as "Take the ninth exit at the roundabout".</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#RIGHT_ROUNDABOUT_PASS">RIGHT_ROUNDABOUT_PASS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Roundabout maneuver (right-hand traffic), such as "Pass the roundabout".</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#RIGHT_TURN">RIGHT_TURN</a></code></div>
<div class="col-last even-row-color">
<div class="block">Right turn maneuver, such as "Turn right".</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#RIGHT_U_TURN">RIGHT_U_TURN</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Right u-turn maneuver, such as "Make a U-turn".</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#SHARP_LEFT_TURN">SHARP_LEFT_TURN</a></code></div>
<div class="col-last even-row-color">
<div class="block">Sharp left turn maneuver, such as "Turn sharply left".</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#SHARP_RIGHT_TURN">SHARP_RIGHT_TURN</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Sharp right turn maneuver, such as "Turn sharply right".</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#SLIGHT_LEFT_TURN">SLIGHT_LEFT_TURN</a></code></div>
<div class="col-last even-row-color">
<div class="block">Slight left turn maneuver, such as "Turn slightly left".</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#SLIGHT_RIGHT_TURN">SLIGHT_RIGHT_TURN</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Slight right turn maneuver, such as "Turn slightly right".</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#valueOf(java.lang.String)">valueOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the enum constant of this class with the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#values()">values</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Enum">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)" title="class or interface in java.lang">compareTo</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()" title="class or interface in java.lang">describeConstable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()" title="class or interface in java.lang">getDeclaringClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()" title="class or interface in java.lang">name</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()" title="class or interface in java.lang">ordinal</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)" title="class or interface in java.lang">valueOf</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ ENUM CONSTANT DETAIL =========== -->
<li>
<section class="constant-details" id="enum-constant-detail">

<ul class="member-list">
<li>
<section class="detail" id="DEPART">
<h3>DEPART</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">DEPART</span></div>
<div class="block"><p>Departure maneuver, such as "Head towards".</p></div>
</section>
</li>
<li>
<section class="detail" id="ARRIVE">
<h3>ARRIVE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">ARRIVE</span></div>
<div class="block"><p>Arrival maneuver, such as "You have reached your destination/waypoint".</p></div>
</section>
</li>
<li>
<section class="detail" id="LEFT_U_TURN">
<h3>LEFT_U_TURN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">LEFT_U_TURN</span></div>
<div class="block"><p>Left-hand U-turn maneuver, such as "Make a U-turn".</p></div>
</section>
</li>
<li>
<section class="detail" id="SHARP_LEFT_TURN">
<h3>SHARP_LEFT_TURN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">SHARP_LEFT_TURN</span></div>
<div class="block"><p>Sharp left turn maneuver, such as "Turn sharply left".</p></div>
</section>
</li>
<li>
<section class="detail" id="LEFT_TURN">
<h3>LEFT_TURN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">LEFT_TURN</span></div>
<div class="block"><p>Left turn maneuver, such as "Turn left".</p></div>
</section>
</li>
<li>
<section class="detail" id="SLIGHT_LEFT_TURN">
<h3>SLIGHT_LEFT_TURN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">SLIGHT_LEFT_TURN</span></div>
<div class="block"><p>Slight left turn maneuver, such as "Turn slightly left".</p></div>
</section>
</li>
<li>
<section class="detail" id="CONTINUE_ON">
<h3>CONTINUE_ON</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">CONTINUE_ON</span></div>
<div class="block"><p>Continue maneuver, such as "Continue straight ahead".</p></div>
</section>
</li>
<li>
<section class="detail" id="SLIGHT_RIGHT_TURN">
<h3>SLIGHT_RIGHT_TURN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">SLIGHT_RIGHT_TURN</span></div>
<div class="block"><p>Slight right turn maneuver, such as "Turn slightly right".</p></div>
</section>
</li>
<li>
<section class="detail" id="RIGHT_TURN">
<h3>RIGHT_TURN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">RIGHT_TURN</span></div>
<div class="block"><p>Right turn maneuver, such as "Turn right".</p></div>
</section>
</li>
<li>
<section class="detail" id="SHARP_RIGHT_TURN">
<h3>SHARP_RIGHT_TURN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">SHARP_RIGHT_TURN</span></div>
<div class="block"><p>Sharp right turn maneuver, such as "Turn sharply right".</p></div>
</section>
</li>
<li>
<section class="detail" id="RIGHT_U_TURN">
<h3>RIGHT_U_TURN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">RIGHT_U_TURN</span></div>
<div class="block"><p>Right u-turn maneuver, such as "Make a U-turn".</p></div>
</section>
</li>
<li>
<section class="detail" id="LEFT_EXIT">
<h3>LEFT_EXIT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">LEFT_EXIT</span></div>
<div class="block"><p>Left exit maneuver, such as "Take the exit".</p></div>
</section>
</li>
<li>
<section class="detail" id="RIGHT_EXIT">
<h3>RIGHT_EXIT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">RIGHT_EXIT</span></div>
<div class="block"><p>Right exit maneuver, such as "Take the exit".</p></div>
</section>
</li>
<li>
<section class="detail" id="LEFT_RAMP">
<h3>LEFT_RAMP</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">LEFT_RAMP</span></div>
<div class="block"><p>Left ramp maneuver, such as "Join the highway".</p></div>
</section>
</li>
<li>
<section class="detail" id="RIGHT_RAMP">
<h3>RIGHT_RAMP</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">RIGHT_RAMP</span></div>
<div class="block"><p>Right ramp maneuver, such as "Join the highway".</p></div>
</section>
</li>
<li>
<section class="detail" id="LEFT_FORK">
<h3>LEFT_FORK</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">LEFT_FORK</span></div>
<div class="block"><p>Left fork maneuver, such as "Keep left".</p></div>
</section>
</li>
<li>
<section class="detail" id="MIDDLE_FORK">
<h3>MIDDLE_FORK</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">MIDDLE_FORK</span></div>
<div class="block"><p>Middle fork maneuver, such as "Keep middle".</p></div>
</section>
</li>
<li>
<section class="detail" id="RIGHT_FORK">
<h3>RIGHT_FORK</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">RIGHT_FORK</span></div>
<div class="block"><p>Right fork maneuver, such as "Keep right".</p></div>
</section>
</li>
<li>
<section class="detail" id="ENTER_HIGHWAY_FROM_LEFT">
<h3>ENTER_HIGHWAY_FROM_LEFT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">ENTER_HIGHWAY_FROM_LEFT</span></div>
<div class="block"><p>Merge onto a highway from the left side. Such a maneuver occurs only in countries that drive on the left side of the road (left-hand traffic).
 </p><p><strong>Note:</strong> This action is only generated when using the Navigate license. On top, until release of HERE SDK 4.16.0,
 it needs to be enabled via <code>RouteOptions</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="ENTER_HIGHWAY_FROM_RIGHT">
<h3>ENTER_HIGHWAY_FROM_RIGHT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">ENTER_HIGHWAY_FROM_RIGHT</span></div>
<div class="block"><p>Merge onto a highway from the right side. Such a maneuver occurs only in countries that drive on the right side of the road (right-hand traffic).
 </p><p><strong>Note:</strong> This action is only generated when using the Navigate license. On top, until release of HERE SDK 4.16.0,
 it needs to be enabled via <code>RouteOptions</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="LEFT_ROUNDABOUT_ENTER">
<h3>LEFT_ROUNDABOUT_ENTER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">LEFT_ROUNDABOUT_ENTER</span></div>
<div class="block"><p>Roundabout maneuver (left-hand traffic), such as "Enter the roundabout".</p></div>
</section>
</li>
<li>
<section class="detail" id="RIGHT_ROUNDABOUT_ENTER">
<h3>RIGHT_ROUNDABOUT_ENTER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">RIGHT_ROUNDABOUT_ENTER</span></div>
<div class="block"><p>Roundabout maneuver (right-hand traffic), such as "Enter the roundabout".</p></div>
</section>
</li>
<li>
<section class="detail" id="LEFT_ROUNDABOUT_PASS">
<h3>LEFT_ROUNDABOUT_PASS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">LEFT_ROUNDABOUT_PASS</span></div>
<div class="block"><p>Roundabout maneuver (left-hand traffic), such as "Pass the roundabout".</p></div>
</section>
</li>
<li>
<section class="detail" id="RIGHT_ROUNDABOUT_PASS">
<h3>RIGHT_ROUNDABOUT_PASS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">RIGHT_ROUNDABOUT_PASS</span></div>
<div class="block"><p>Roundabout maneuver (right-hand traffic), such as "Pass the roundabout".</p></div>
</section>
</li>
<li>
<section class="detail" id="LEFT_ROUNDABOUT_EXIT1">
<h3>LEFT_ROUNDABOUT_EXIT1</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">LEFT_ROUNDABOUT_EXIT1</span></div>
<div class="block"><p>Roundabout maneuver (left-hand traffic), such as  "Take the first exit at the roundabout".</p></div>
</section>
</li>
<li>
<section class="detail" id="LEFT_ROUNDABOUT_EXIT2">
<h3>LEFT_ROUNDABOUT_EXIT2</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">LEFT_ROUNDABOUT_EXIT2</span></div>
<div class="block"><p>Roundabout maneuver (left-hand traffic), such as "Take the second exit at the roundabout".</p></div>
</section>
</li>
<li>
<section class="detail" id="LEFT_ROUNDABOUT_EXIT3">
<h3>LEFT_ROUNDABOUT_EXIT3</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">LEFT_ROUNDABOUT_EXIT3</span></div>
<div class="block"><p>Roundabout maneuver (left-hand traffic), such as "Take the third exit at the roundabout".</p></div>
</section>
</li>
<li>
<section class="detail" id="LEFT_ROUNDABOUT_EXIT4">
<h3>LEFT_ROUNDABOUT_EXIT4</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">LEFT_ROUNDABOUT_EXIT4</span></div>
<div class="block"><p>Roundabout maneuver (left-hand traffic), such as "Take the fourth exit at the roundabout".</p></div>
</section>
</li>
<li>
<section class="detail" id="LEFT_ROUNDABOUT_EXIT5">
<h3>LEFT_ROUNDABOUT_EXIT5</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">LEFT_ROUNDABOUT_EXIT5</span></div>
<div class="block"><p>Roundabout maneuver (left-hand traffic), such as "Take the fifth exit at the roundabout".</p></div>
</section>
</li>
<li>
<section class="detail" id="LEFT_ROUNDABOUT_EXIT6">
<h3>LEFT_ROUNDABOUT_EXIT6</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">LEFT_ROUNDABOUT_EXIT6</span></div>
<div class="block"><p>Roundabout maneuver (left-hand traffic), such as "Take the sixth exit at the roundabout".</p></div>
</section>
</li>
<li>
<section class="detail" id="LEFT_ROUNDABOUT_EXIT7">
<h3>LEFT_ROUNDABOUT_EXIT7</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">LEFT_ROUNDABOUT_EXIT7</span></div>
<div class="block"><p>Roundabout maneuver (left-hand traffic), such as "Take the seventh exit at the roundabout".</p></div>
</section>
</li>
<li>
<section class="detail" id="LEFT_ROUNDABOUT_EXIT8">
<h3>LEFT_ROUNDABOUT_EXIT8</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">LEFT_ROUNDABOUT_EXIT8</span></div>
<div class="block"><p>Roundabout maneuver (left-hand traffic), such as "Take the eighth exit at the roundabout".</p></div>
</section>
</li>
<li>
<section class="detail" id="LEFT_ROUNDABOUT_EXIT9">
<h3>LEFT_ROUNDABOUT_EXIT9</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">LEFT_ROUNDABOUT_EXIT9</span></div>
<div class="block"><p>Roundabout maneuver (left-hand traffic), such as "Take the ninth exit at the roundabout".</p></div>
</section>
</li>
<li>
<section class="detail" id="LEFT_ROUNDABOUT_EXIT10">
<h3>LEFT_ROUNDABOUT_EXIT10</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">LEFT_ROUNDABOUT_EXIT10</span></div>
<div class="block"><p>Roundabout maneuver (left-hand traffic), such as "Take the tenth exit at the roundabout".</p></div>
</section>
</li>
<li>
<section class="detail" id="LEFT_ROUNDABOUT_EXIT11">
<h3>LEFT_ROUNDABOUT_EXIT11</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">LEFT_ROUNDABOUT_EXIT11</span></div>
<div class="block"><p>Roundabout maneuver (left-hand traffic), such as "Take the eleventh exit at the roundabout".</p></div>
</section>
</li>
<li>
<section class="detail" id="LEFT_ROUNDABOUT_EXIT12">
<h3>LEFT_ROUNDABOUT_EXIT12</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">LEFT_ROUNDABOUT_EXIT12</span></div>
<div class="block"><p>Roundabout maneuver (left-hand traffic), such as "Take the twelfth exit at the roundabout".</p></div>
</section>
</li>
<li>
<section class="detail" id="RIGHT_ROUNDABOUT_EXIT1">
<h3>RIGHT_ROUNDABOUT_EXIT1</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">RIGHT_ROUNDABOUT_EXIT1</span></div>
<div class="block"><p>Roundabout maneuver (right-hand traffic), such as "Take the first exit at the roundabout".</p></div>
</section>
</li>
<li>
<section class="detail" id="RIGHT_ROUNDABOUT_EXIT2">
<h3>RIGHT_ROUNDABOUT_EXIT2</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">RIGHT_ROUNDABOUT_EXIT2</span></div>
<div class="block"><p>Roundabout maneuver (right-hand traffic), such as "Take the second exit at the roundabout".</p></div>
</section>
</li>
<li>
<section class="detail" id="RIGHT_ROUNDABOUT_EXIT3">
<h3>RIGHT_ROUNDABOUT_EXIT3</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">RIGHT_ROUNDABOUT_EXIT3</span></div>
<div class="block"><p>Roundabout maneuver (right-hand traffic), such as "Take the third exit at the roundabout".</p></div>
</section>
</li>
<li>
<section class="detail" id="RIGHT_ROUNDABOUT_EXIT4">
<h3>RIGHT_ROUNDABOUT_EXIT4</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">RIGHT_ROUNDABOUT_EXIT4</span></div>
<div class="block"><p>Roundabout maneuver (right-hand traffic), such as "Take the fourth exit at the roundabout".</p></div>
</section>
</li>
<li>
<section class="detail" id="RIGHT_ROUNDABOUT_EXIT5">
<h3>RIGHT_ROUNDABOUT_EXIT5</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">RIGHT_ROUNDABOUT_EXIT5</span></div>
<div class="block"><p>Roundabout maneuver (right-hand traffic), such as "Take the fifth exit at the roundabout".</p></div>
</section>
</li>
<li>
<section class="detail" id="RIGHT_ROUNDABOUT_EXIT6">
<h3>RIGHT_ROUNDABOUT_EXIT6</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">RIGHT_ROUNDABOUT_EXIT6</span></div>
<div class="block"><p>Roundabout maneuver (right-hand traffic), such as "Take the sixth exit at the roundabout".</p></div>
</section>
</li>
<li>
<section class="detail" id="RIGHT_ROUNDABOUT_EXIT7">
<h3>RIGHT_ROUNDABOUT_EXIT7</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">RIGHT_ROUNDABOUT_EXIT7</span></div>
<div class="block"><p>Roundabout maneuver (right-hand traffic), such as "Take the seventh exit at the roundabout".</p></div>
</section>
</li>
<li>
<section class="detail" id="RIGHT_ROUNDABOUT_EXIT8">
<h3>RIGHT_ROUNDABOUT_EXIT8</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">RIGHT_ROUNDABOUT_EXIT8</span></div>
<div class="block"><p>Roundabout maneuver (right-hand traffic), such as "Take the eighth exit at the roundabout".</p></div>
</section>
</li>
<li>
<section class="detail" id="RIGHT_ROUNDABOUT_EXIT9">
<h3>RIGHT_ROUNDABOUT_EXIT9</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">RIGHT_ROUNDABOUT_EXIT9</span></div>
<div class="block"><p>Roundabout maneuver (right-hand traffic), such as "Take the ninth exit at the roundabout".</p></div>
</section>
</li>
<li>
<section class="detail" id="RIGHT_ROUNDABOUT_EXIT10">
<h3>RIGHT_ROUNDABOUT_EXIT10</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">RIGHT_ROUNDABOUT_EXIT10</span></div>
<div class="block"><p>Roundabout maneuver (right-hand traffic), such as "Take the tenth exit at the roundabout".</p></div>
</section>
</li>
<li>
<section class="detail" id="RIGHT_ROUNDABOUT_EXIT11">
<h3>RIGHT_ROUNDABOUT_EXIT11</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">RIGHT_ROUNDABOUT_EXIT11</span></div>
<div class="block"><p>Roundabout maneuver (right-hand traffic), such as "Take the eleventh exit at the roundabout".</p></div>
</section>
</li>
<li>
<section class="detail" id="RIGHT_ROUNDABOUT_EXIT12">
<h3>RIGHT_ROUNDABOUT_EXIT12</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">RIGHT_ROUNDABOUT_EXIT12</span></div>
<div class="block"><p>Roundabout maneuver (right-hand traffic), such as "Take the twelfth exit at the roundabout".</p></div>
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
<section class="detail" id="values()">
<h3>values</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a>[]</span> <span class="element-name">values</span>()</div>
<div class="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>an array containing the constants of this enum class, in the order they are declared</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="valueOf(java.lang.String)">
<h3>valueOf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuveraction" title="enum class in com.here.sdk.routing">ManeuverAction</a></span> <span class="element-name">valueOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns the enum constant of this class with the specified name.
The string must match <i>exactly</i> an identifier used to declare an
enum constant in this class.  (Extraneous whitespace characters are 
not permitted.)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name of the enum constant to be returned.</dd>
<dt>Returns:</dt>
<dd>the enum constant with the specified name</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if this enum class has no constant with the specified name</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang">NullPointerException</a></code> - if the argument is null</dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->






</div>
`
}</HTMLBlock>
