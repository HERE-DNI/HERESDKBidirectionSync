---
title: "IconProvider (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-iconprovider"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- IconProvider.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance">com.here.sdk.mapview.IconProvider</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public class </span><span className="element-name type-name-label">IconProvider</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div className="block">This provider creates icons from a given set of parameters for map content and constraints for
 icon dimensions for a particular map scheme. The icon creation currently does not rely on map
 data. Therefore, it works without online connection.

 Note: This feature is in BETA state and thus there can be bugs and unexpected behavior.
 Related APIs may change for new releases without a deprecation process.</div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static interface </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-iconprovider-iconcallback" title="interface in com.here.sdk.mapview">IconProvider.IconCallback</a></code></div>
<div className="col-last even-row-color">
<div className="block">Interface which is used as callback to pass back an image or error code after calling
 the createRoadShieldIcon() method.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-iconprovider#%3Cinit%3E(com.here.sdk.mapview.MapContext)">IconProvider</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> mapContext)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates an IconProvider.</div>
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
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapContext)">
<h3>IconProvider</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">IconProvider</span><wbr/><span className="parameters">(<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> mapContext)</span></div>
<div className="block">Creates an IconProvider.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>mapContext</code> - The map context instance.</dd>
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
<section className="detail" id="createRoadShieldIcon(com.here.sdk.mapview.RoadShieldIconProperties,com.here.sdk.mapview.MapScheme,com.here.sdk.mapview.IconProviderAssetType,long,long,com.here.sdk.mapview.IconProvider.IconCallback)">
<h3>createRoadShieldIcon</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">createRoadShieldIcon</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-roadshieldiconproperties" title="class in com.here.sdk.mapview">RoadShieldIconProperties</a> properties,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscheme" title="enum class in com.here.sdk.mapview">MapScheme</a> mapScheme,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-iconproviderassettype" title="enum class in com.here.sdk.mapview">IconProviderAssetType</a> assetType,
 long widthConstraintInPixels,
 long heightConstraintInPixels,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-iconprovider-iconcallback" title="interface in com.here.sdk.mapview">IconProvider.IconCallback</a> callback)</span></div>
<div className="block">Creates an image displaying a road shield according to the given parameters.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>properties</code> - The properties which determine the kind of road shield to be created.</dd>
<dd><code>mapScheme</code> - The map scheme for which the road shield should be created.</dd>
<dd><code>assetType</code> - The asset type for which the road shield should be created.</dd>
<dd><code>widthConstraintInPixels</code> - The maximum width of the road shield in pixels.
 The value is capped to a maximum of 4096 pixels. The image will be created as large as
 possible within the width and height constraints while maintaining the aspect ratio.
 If set to 0, the width will be calculated based on the heightConstraintInPixels to
 preserve the aspect ratio.</dd>
<dd><code>heightConstraintInPixels</code> - The maximum height of the road shield in pixels.
 The value is capped to a maximum of 4096 pixels. The image will be created as large as
 possible within the width and height constraints while maintaining the aspect ratio.
 If set to 0, the original image-asset's height will be used.</dd>
<dd><code>callback</code> - The callback which is used to return the created image or an error code.

 Note: This feature is in BETA state and thus there can be bugs and unexpected behavior.
 Related APIs may change for new releases without a deprecation process.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="createVehicleRestrictionIcon(com.here.sdk.mapview.PickMapContentResult.VehicleRestrictionResult,com.here.sdk.mapview.MapScheme,com.here.sdk.mapview.IconProviderAssetType,com.here.sdk.core.Size2D,com.here.sdk.mapview.IconProvider.IconCallback)">
<h3>createVehicleRestrictionIcon</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">createVehicleRestrictionIcon</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-pickmapcontentresult-vehiclerestrictionresult" title="class in com.here.sdk.mapview">PickMapContentResult.VehicleRestrictionResult</a> pickingResult,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscheme" title="enum class in com.here.sdk.mapview">MapScheme</a> mapScheme,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-iconproviderassettype" title="enum class in com.here.sdk.mapview">IconProviderAssetType</a> assetType,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-size2d" title="class in com.here.sdk.core">Size2D</a> sizeConstraintsInPixels,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-iconprovider-iconcallback" title="interface in com.here.sdk.mapview">IconProvider.IconCallback</a> callback)</span></div>
<div className="block">Creates an image representing a vehicle restriction as shown on the map, based on map content
 picking result.</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>pickingResult</code> - The result of picking vehicle restrictions.</dd>
<dd><code>mapScheme</code> - The map scheme for which the vehicle restriction icon should be created.</dd>
<dd><code>assetType</code> - The asset type for which the vehicle restriction icon should be created.</dd>
<dd><code>sizeConstraintsInPixels</code> - The maximum width and height of the icon in pixels.
 The values are capped to a maximum of 4096 pixels. The image will be created as large as
 possible within the width and height constraints while maintaining the aspect ratio.
 If either width or height is set to 0, it will be calculated automatically based on icon's
 aspect ratio.</dd>
<dd><code>callback</code> - The callback which is used to return the created image, or an error code.</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="createVehicleRestrictionIcon(com.here.sdk.mapview.VehicleRestrictionIconProperties,com.here.sdk.mapview.MapScheme,com.here.sdk.mapview.IconProviderAssetType,com.here.sdk.core.Size2D,com.here.sdk.mapview.IconProvider.IconCallback)">
<h3>createVehicleRestrictionIcon</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">createVehicleRestrictionIcon</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-vehiclerestrictioniconproperties" title="class in com.here.sdk.mapview">VehicleRestrictionIconProperties</a> iconProperties,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapscheme" title="enum class in com.here.sdk.mapview">MapScheme</a> mapScheme,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-iconproviderassettype" title="enum class in com.here.sdk.mapview">IconProviderAssetType</a> assetType,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-size2d" title="class in com.here.sdk.core">Size2D</a> sizeConstraintsInPixels,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-iconprovider-iconcallback" title="interface in com.here.sdk.mapview">IconProvider.IconCallback</a> callback)</span></div>
<div className="block">Creates an image representing a vehicle restriction as shown on the map.
 <p>
 In case when `VehicleRestriction` object specifies multiple types of restrictions, then the
 icon is generated for the first one according to the following priority: <a href="sdk-for-android-navigate-vehiclerestriction#restriction"><code>VehicleRestriction.restriction</code></a>,
 <a href="sdk-for-android-navigate-vehiclerestriction#axleCount"><code>VehicleRestriction.axleCount</code></a>, <a href="sdk-for-android-navigate-vehiclerestriction#axleCountInGroup"><code>VehicleRestriction.axleCountInGroup</code></a>,
 <a href="sdk-for-android-navigate-vehiclerestriction#hazmatRestriction"><code>VehicleRestriction.hazmatRestriction</code></a>, <a href="sdk-for-android-navigate-vehiclerestriction#trailerCount"><code>VehicleRestriction.trailerCount</code></a>.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>iconProperties</code> - The properties of the icon.</dd>
<dd><code>mapScheme</code> - The map scheme for which the vehicle restriction icon should be created.</dd>
<dd><code>assetType</code> - The asset type for which the vehicle restriction icon should be created.</dd>
<dd><code>sizeConstraintsInPixels</code> - The maximum width and height of the icon in pixels.
 The values are capped to a maximum of 4096 pixels. The image will be created as large as
 possible within the width and height constraints while maintaining the aspect ratio.
 If either width or height is set to 0, it will be calculated automatically based on icon's
 aspect ratio.</dd>
<dd><code>callback</code> - The callback which is used to return the created image, or an error code.</dd>
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
