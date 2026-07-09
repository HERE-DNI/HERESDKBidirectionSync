---
title: "TruckRestrictionWarning (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TruckRestrictionWarning.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.navigation.TruckRestrictionWarning</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">TruckRestrictionWarning</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block"><p>Represents truck restrictions. For example, there can be a bridge ahead not high enough to pass a big truck
 or there can be a road ahead where the truck’s weight exceeds the permissible limit.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section className="field-summary" id="field-summary">

<div className="caption"><span>Fields</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning#axleCount">axleCount</a></code></div>
<div className="col-last even-row-color">
<div className="block">The axle count for which the current restriction applies.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-dimensionrestriction" title="class in com.here.sdk.navigation">DimensionRestriction</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning#dimensionRestriction">dimensionRestriction</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Vehicle dimension restrictions.</div>
</div>
<div className="col-first even-row-color"><code>double</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning#distanceInMeters">distanceInMeters</a></code></div>
<div className="col-last even-row-color">
<div className="block">The distance from the current location to the restriction.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning#distanceType">distanceType</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Indicates if the specified truck restriction is ahead of the vehicle or has just passed by.</div>
</div>
<div className="col-first even-row-color"><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-transport-hazardousmaterial" title="enum class in com.here.sdk.transport">HazardousMaterial</a>&gt;</code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning#hazardousMaterials">hazardousMaterials</a></code></div>
<div className="col-last even-row-color">
<div className="block">The list of hazardous materials which are restricted on the road section for which the warning applies.</div>
</div>
<div className="col-first odd-row-color"><code>int</code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning#id">id</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Unique identifier for this specific truck restriction warning instance.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-timerule" title="class in com.here.sdk.core">TimeRule</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning#timeRule">timeRule</a></code></div>
<div className="col-last even-row-color">
<div className="block">Time rule indicating the time periods for which the restriction applies.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning#trailerCount">trailerCount</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The trailer count for which the current restriction applies.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-transport-truckroadtype" title="enum class in com.here.sdk.transport">TruckRoadType</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning#truckRoadType">truckRoadType</a></code></div>
<div className="col-last even-row-color">
<div className="block">Truck road type restriction.</div>
</div>
<div className="col-first odd-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-transport-tunnelcategory" title="enum class in com.here.sdk.transport">TunnelCategory</a></code></div>
<div className="col-second odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning#tunnelCategory">tunnelCategory</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Tunnel category.</div>
</div>
<div className="col-first even-row-color"><code><a href="sdk-for-android-navigate-com-here-sdk-navigation-weightrestriction" title="class in com.here.sdk.navigation">WeightRestriction</a></code></div>
<div className="col-second even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning#weightRestriction">weightRestriction</a></code></div>
<div className="col-last even-row-color">
<div className="block">Weight restriction.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning#%3Cinit%3E(double,com.here.sdk.navigation.DistanceType)">TruckRestrictionWarning</a><wbr/>(double distanceInMeters,
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a> distanceType)</code></div>
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
<section className="detail" id="id">
<h3>id</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">id</span></div>
<div className="block"><p>Unique identifier for this specific truck restriction warning instance.
 Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
 Use this ID to track, update, or dismiss individual warning instances of this type.</p></div>
</section>
</li>
<li>
<section className="detail" id="distanceInMeters">
<h3>distanceInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">double</span> <span className="element-name">distanceInMeters</span></div>
<div className="block"><p>The distance from the current location to the restriction.</p></div>
</section>
</li>
<li>
<section className="detail" id="weightRestriction">
<h3>weightRestriction</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-weightrestriction" title="class in com.here.sdk.navigation">WeightRestriction</a></span> <span className="element-name">weightRestriction</span></div>
<div className="block"><p>Weight restriction.
 It is <code>null</code> when there is no known weight restriction ahead.</p></div>
</section>
</li>
<li>
<section className="detail" id="dimensionRestriction">
<h3>dimensionRestriction</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-dimensionrestriction" title="class in com.here.sdk.navigation">DimensionRestriction</a></span> <span className="element-name">dimensionRestriction</span></div>
<div className="block"><p>Vehicle dimension restrictions.
 It is <code>null</code> when there is no known dimension restriction ahead.</p></div>
</section>
</li>
<li>
<section className="detail" id="distanceType">
<h3>distanceType</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a></span> <span className="element-name">distanceType</span></div>
<div className="block"><p>Indicates if the specified truck restriction is ahead of the vehicle or has just passed by. If it is ahead, then <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning#distanceInMeters"><code>distanceInMeters</code></a> is greater than 0.</p></div>
</section>
</li>
<li>
<section className="detail" id="trailerCount">
<h3>trailerCount</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></span> <span className="element-name">trailerCount</span></div>
<div className="block"><p>The trailer count for which the current restriction applies.
 If the field is 'null' then the current restriction does not have a condition based on trailers count.</p></div>
</section>
</li>
<li>
<section className="detail" id="timeRule">
<h3>timeRule</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-timerule" title="class in com.here.sdk.core">TimeRule</a></span> <span className="element-name">timeRule</span></div>
<div className="block"><p>Time rule indicating the time periods for which the restriction applies.
 If the field is 'null' then the restriction is applicable at anytime.</p></div>
</section>
</li>
<li>
<section className="detail" id="truckRoadType">
<h3>truckRoadType</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-truckroadtype" title="enum class in com.here.sdk.transport">TruckRoadType</a></span> <span className="element-name">truckRoadType</span></div>
<div className="block"><p>Truck road type restriction.</p></div>
</section>
</li>
<li>
<section className="detail" id="hazardousMaterials">
<h3>hazardousMaterials</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-transport-hazardousmaterial" title="enum class in com.here.sdk.transport">HazardousMaterial</a>&gt;</span> <span className="element-name">hazardousMaterials</span></div>
<div className="block"><p>The list of hazardous materials which are restricted on the road section for which the warning applies.</p></div>
</section>
</li>
<li>
<section className="detail" id="tunnelCategory">
<h3>tunnelCategory</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-transport-tunnelcategory" title="enum class in com.here.sdk.transport">TunnelCategory</a></span> <span className="element-name">tunnelCategory</span></div>
<div className="block"><p>Tunnel category.</p></div>
</section>
</li>
<li>
<section className="detail" id="axleCount">
<h3>axleCount</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-integerrange" title="class in com.here.sdk.core">IntegerRange</a></span> <span className="element-name">axleCount</span></div>
<div className="block"><p>The axle count for which the current restriction applies.
 If this field is <code>null</code>, the restriction does not depend on axle count.</p></div>
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
<section className="detail" id="&lt;init&gt;(double,com.here.sdk.navigation.DistanceType)">
<h3>TruckRestrictionWarning</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">TruckRestrictionWarning</span><wbr/><span className="parameters">(double distanceInMeters,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-distancetype" title="enum class in com.here.sdk.navigation">DistanceType</a> distanceType)</span></div>
<div className="block"><p>Creates a new instance.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>distanceInMeters</code> - <p>The distance from the current location to the restriction.</p></dd>
<dd><code>distanceType</code> - <p>Indicates if the specified truck restriction is ahead of the vehicle or has just passed by. If it is ahead, then <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning#distanceInMeters"><code>distanceInMeters</code></a> is greater than 0.</p></dd>
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
<li>
<section className="detail" id="isGeneral()">
<h3>isGeneral</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">boolean</span> <span className="element-name">isGeneral</span>()</div>
<div className="block"><p>Checks if this truck restriction warning is general.
 A general warning has no specific restriction conditions set.
 Please note that time rule still might be set for a general warning, but it is not considered as a specific restriction condition.
 This method only checks that no specific conditions are set for the warning.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p><code>true</code> if all restriction fields are null or empty, <code>false</code> otherwise.</p></dd>
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
