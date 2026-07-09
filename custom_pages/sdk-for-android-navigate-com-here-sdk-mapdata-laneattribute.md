---
title: "LaneAttribute (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-laneattribute"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- LaneAttribute.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapdata</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.mapdata.LaneAttribute</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">LaneAttribute</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>A class that describes attributes assigned to a specific section of a lane.
 It includes lane markings, allowed travel directions, tolling info, access restrictions, and optional lane type.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess" title="class in com.here.sdk.navigation">LaneAccess</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-laneattribute#access">access</a></code></div>
<div className="col-last even-row-color">
<div className="block">Access characteristics of the lane that identifies the vehicle type(s) allowed to access a lane.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-lanemarkings" title="class in com.here.sdk.navigation">LaneMarkings</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-laneattribute#markings">markings</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Indicate the markings on the road</div>
</div>
<div className="col-first even-row-color"><code>int</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-laneattribute#startOffsetInMeters">startOffsetInMeters</a></code></div>
<div className="col-last even-row-color">
<div className="block">The start offset of the lane in meters from the beginning of the segment</div>
</div>
<div className="col-first odd-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapdata-tollstructure" title="class in com.here.sdk.mapdata">TollStructure</a>&gt;</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-laneattribute#tollStructures">tollStructures</a></code></div>
<div className="col-last odd-row-color">
<div className="block">List of Toll Structure that identifies the presence of physical toll structures or automatic controls on the lane
 at entry and exit points along a toll road which requires payment (cash, electronic, etc.) or ticket</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype" title="class in com.here.sdk.navigation">LaneType</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-laneattribute#type">type</a></code></div>
<div className="col-last even-row-color">
<div className="block">Specifies the functional and regulatory roles a lane may serve, such as turn, express, HOV, or bike use</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-laneattribute#%3Cinit%3E(int,com.here.sdk.navigation.LaneMarkings,com.here.sdk.navigation.LaneAccess,java.util.List)">LaneAttribute</a><wbr/>(int startOffsetInMeters,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanemarkings" title="class in com.here.sdk.navigation">LaneMarkings</a> markings,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess" title="class in com.here.sdk.navigation">LaneAccess</a> access,
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapdata-tollstructure" title="class in com.here.sdk.mapdata">TollStructure</a>&gt; tollStructures)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section className="field-details" id="field-detail">

<ul className="member-list">
<li>
<section className="detail" id="startOffsetInMeters">
<h3>startOffsetInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">startOffsetInMeters</span></div>
<div className="block"><p>The start offset of the lane in meters from the beginning of the segment</p></div>
</section>
</li>
<li>
<section className="detail" id="markings">
<h3>markings</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-lanemarkings" title="class in com.here.sdk.navigation">LaneMarkings</a></span> <span className="element-name">markings</span></div>
<div className="block"><p>Indicate the markings on the road</p></div>
</section>
</li>
<li>
<section className="detail" id="access">
<h3>access</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess" title="class in com.here.sdk.navigation">LaneAccess</a></span> <span className="element-name">access</span></div>
<div className="block"><p>Access characteristics of the lane that identifies the vehicle type(s) allowed to access a lane.</p></div>
</section>
</li>
<li>
<section className="detail" id="tollStructures">
<h3>tollStructures</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapdata-tollstructure" title="class in com.here.sdk.mapdata">TollStructure</a>&gt;</span> <span className="element-name">tollStructures</span></div>
<div className="block"><p>List of Toll Structure that identifies the presence of physical toll structures or automatic controls on the lane
 at entry and exit points along a toll road which requires payment (cash, electronic, etc.) or ticket</p></div>
</section>
</li>
<li>
<section className="detail" id="type">
<h3>type</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-lanetype" title="class in com.here.sdk.navigation">LaneType</a></span> <span className="element-name">type</span></div>
<div className="block"><p>Specifies the functional and regulatory roles a lane may serve, such as turn, express, HOV, or bike use</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(int,com.here.sdk.navigation.LaneMarkings,com.here.sdk.navigation.LaneAccess,java.util.List)">
<h3>LaneAttribute</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">LaneAttribute</span><wbr/><span className="parameters">(int startOffsetInMeters,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-lanemarkings" title="class in com.here.sdk.navigation">LaneMarkings</a> markings,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-laneaccess" title="class in com.here.sdk.navigation">LaneAccess</a> access,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapdata-tollstructure" title="class in com.here.sdk.mapdata">TollStructure</a>&gt; tollStructures)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>startOffsetInMeters</code> - <p>The start offset of the lane in meters from the beginning of the segment</p></dd>
<dd><code>markings</code> - <p>Indicate the markings on the road</p></dd>
<dd><code>access</code> - <p>Access characteristics of the lane that identifies the vehicle type(s) allowed to access a lane.</p></dd>
<dd><code>tollStructures</code> - <p>List of Toll Structure that identifies the presence of physical toll structures or automatic controls on the lane
 at entry and exit points along a toll road which requires payment (cash, electronic, etc.) or ticket</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">equals</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="hashCode()">
<h3>hashCode</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">hashCode</span>()</div>
<dl className="notes">
<dt>Overrides:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
</div>



</div>
`
}</HTMLBlock>
