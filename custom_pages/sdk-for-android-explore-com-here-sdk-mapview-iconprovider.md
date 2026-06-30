---
title: "IconProvider (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-iconprovider"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- IconProvider.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.mapview.IconProvider</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">IconProvider</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block">This provider creates icons from a given set of parameters for map content and constraints for
 icon dimensions for a particular map scheme. The icon creation currently does not rely on map
 data. Therefore, it works without online connection.

 Note: This feature is in BETA state and thus there can be bugs and unexpected behavior.
 Related APIs may change for new releases without a deprecation process.</div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static interface </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-iconprovider-iconcallback" title="interface in com.here.sdk.mapview">IconProvider.IconCallback</a></code></div>
<div class="col-last even-row-color">
<div class="block">Interface which is used as callback to pass back an image or error code after calling
 the createRoadShieldIcon() method.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-iconprovider#%3Cinit%3E(com.here.sdk.mapview.MapContext)">IconProvider</a><wbr/>(<a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> mapContext)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates an IconProvider.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-iconprovider#createRoadShieldIcon(com.here.sdk.mapview.RoadShieldIconProperties,com.here.sdk.mapview.MapScheme,com.here.sdk.mapview.IconProviderAssetType,long,long,com.here.sdk.mapview.IconProvider.IconCallback)">createRoadShieldIcon</a><wbr/>(<a href="sdk-for-android-explore-com-here-sdk-mapview-roadshieldiconproperties" title="class in com.here.sdk.mapview">RoadShieldIconProperties</a> properties,
 <a href="sdk-for-android-explore-com-here-sdk-mapview-mapscheme" title="enum class in com.here.sdk.mapview">MapScheme</a> mapScheme,
 <a href="sdk-for-android-explore-com-here-sdk-mapview-iconproviderassettype" title="enum class in com.here.sdk.mapview">IconProviderAssetType</a> assetType,
 long widthConstraintInPixels,
 long heightConstraintInPixels,
 <a href="sdk-for-android-explore-com-here-sdk-mapview-iconprovider-iconcallback" title="interface in com.here.sdk.mapview">IconProvider.IconCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Creates an image displaying a road shield according to the given parameters.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.mapview.MapContext)">
<h3>IconProvider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">IconProvider</span><wbr/><span class="parameters">(<a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview">MapContext</a> mapContext)</span></div>
<div class="block">Creates an IconProvider.</div>
<dl class="notes">
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
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="createRoadShieldIcon(com.here.sdk.mapview.RoadShieldIconProperties,com.here.sdk.mapview.MapScheme,com.here.sdk.mapview.IconProviderAssetType,long,long,com.here.sdk.mapview.IconProvider.IconCallback)">
<h3>createRoadShieldIcon</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">createRoadShieldIcon</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-com-here-sdk-mapview-roadshieldiconproperties" title="class in com.here.sdk.mapview">RoadShieldIconProperties</a> properties,
 @NonNull
 <a href="sdk-for-android-explore-com-here-sdk-mapview-mapscheme" title="enum class in com.here.sdk.mapview">MapScheme</a> mapScheme,
 @NonNull
 <a href="sdk-for-android-explore-com-here-sdk-mapview-iconproviderassettype" title="enum class in com.here.sdk.mapview">IconProviderAssetType</a> assetType,
 long widthConstraintInPixels,
 long heightConstraintInPixels,
 @NonNull
 <a href="sdk-for-android-explore-com-here-sdk-mapview-iconprovider-iconcallback" title="interface in com.here.sdk.mapview">IconProvider.IconCallback</a> callback)</span></div>
<div class="block">Creates an image displaying a road shield according to the given parameters.</div>
<dl class="notes">
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
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->






</div>
`
}</HTMLBlock>
