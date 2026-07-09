---
title: "WarningsRegistry (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-warner-warningsregistry"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- WarningsRegistry.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.warner</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.warner.WarningsRegistry</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">WarningsRegistry</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>A class that store warning metadata for different warning types.
 Aggregates individual collection for each warning category (safety cameras, truck restrictions, etc.).
 Provided by <code>WarnerEngine</code> so callers can lookup detailed information about specific warnings.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="getSafetyCameraWarning(com.here.sdk.warner.Warning)">
<h3>getSafetyCameraWarning</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarning" title="class in com.here.sdk.navigation">SafetyCameraWarning</a></span> <span className="element-name">getSafetyCameraWarning</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span></div>
<div className="block"><p>Returns a safety-camera warning corresponding to the given identifier.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>warning</code> - <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
     The <code>warning</code> uniquely identifies a single safety-camera warning within this registry
     and is used to retrieve its full metadata.</p></dd>
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarning" title="class in com.here.sdk.navigation"><code>SafetyCameraWarning</code></a> object associated with the provided <code>warning</code>,
     or <code>null</code> if no warning exists for the given <code>warning</code>.
     This object contains the full details and attributes of the corresponding warning.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTruckRestrictionWarning(com.here.sdk.warner.Warning)">
<h3>getTruckRestrictionWarning</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning" title="class in com.here.sdk.navigation">TruckRestrictionWarning</a></span> <span className="element-name">getTruckRestrictionWarning</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span></div>
<div className="block"><p>Returns a truck restrictions warning corresponding to the given identifier.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>warning</code> - <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
     The <code>warning</code> uniquely identifies a single truck restrictions warning within this registry
     and is used to retrieve its full metadata.</p></dd>
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning" title="class in com.here.sdk.navigation"><code>TruckRestrictionWarning</code></a> object associated with the provided <code>warning</code>,
     or <code>null</code> if no warning exists for the given <code>warning</code>.
     This object contains the full details and attributes of the corresponding warning.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRoadSignWarning(com.here.sdk.warner.Warning)">
<h3>getRoadSignWarning</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning" title="class in com.here.sdk.navigation">RoadSignWarning</a></span> <span className="element-name">getRoadSignWarning</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span></div>
<div className="block"><p>Returns a road-sign warning corresponding to the given identifier.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>warning</code> - <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
     The <code>warning</code> uniquely identifies a single road sign warning within this registry
     and is used to retrieve its full metadata.</p></dd>
<dt>Returns:</dt>
<dd><p>The <code>sdk.navigation.RoadSignWarning</code> object associated with the provided <code>warning</code>,
     or <code>null</code> if no warning exists for the given <code>warning</code>.
     This object contains the full details and attributes of the corresponding warning.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRealisticViewWarning(com.here.sdk.warner.Warning)">
<h3>getRealisticViewWarning</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning" title="class in com.here.sdk.navigation">RealisticViewWarning</a></span> <span className="element-name">getRealisticViewWarning</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span></div>
<div className="block"><p>Returns a realistic-view warning corresponding to the given identifier.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>warning</code> - <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
     The <code>warning</code> uniquely identifies a single realistic-view warning within this registry
     and is used to retrieve its full metadata.</p></dd>
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning" title="class in com.here.sdk.navigation"><code>RealisticViewWarning</code></a> object associated with the provided <code>warning</code>,
     or <code>null</code> if no warning exists for the given <code>warning</code>.
     This object contains the full details and attributes of the corresponding warning.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getEnvironmentalZoneWarning(com.here.sdk.warner.Warning)">
<h3>getEnvironmentalZoneWarning</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-environmentalzonewarning" title="class in com.here.sdk.navigation">EnvironmentalZoneWarning</a></span> <span className="element-name">getEnvironmentalZoneWarning</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span></div>
<div className="block"><p>Returns environmental zone warning corresponding to the given identifier.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>warning</code> - <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
     The <code>warning</code> uniquely identifies a single environmental zone warning within this registry
     and is used to retrieve its full metadata.</p></dd>
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-navigation-environmentalzonewarning" title="class in com.here.sdk.navigation"><code>EnvironmentalZoneWarning</code></a> object associated with the provided <code>warning</code>,
     or <code>null</code> if no warning exists for the given <code>warning</code>.
     This object contains the full details and attributes of the corresponding warning.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSchoolZoneWarning(com.here.sdk.warner.Warning)">
<h3>getSchoolZoneWarning</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-schoolzonewarning" title="class in com.here.sdk.navigation">SchoolZoneWarning</a></span> <span className="element-name">getSchoolZoneWarning</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span></div>
<div className="block"><p>Returns a school zone warning corresponding to the given identifier.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>warning</code> - <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
     The <code>warning</code> uniquely identifies a single school zone warning within this registry
     and is used to retrieve its full metadata.</p></dd>
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-navigation-schoolzonewarning" title="class in com.here.sdk.navigation"><code>SchoolZoneWarning</code></a> object associated with the provided <code>warning</code>,
     or <code>null</code> if no warning exists for the given <code>warning</code>.
     This object contains the full details and attributes of the corresponding warning.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTollStopWarning(com.here.sdk.warner.Warning)">
<h3>getTollStopWarning</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-tollstop" title="class in com.here.sdk.navigation">TollStop</a></span> <span className="element-name">getTollStopWarning</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span></div>
<div className="block"><p>Returns a toll stop warning corresponding to the given identifier.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>warning</code> - <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
     The <code>warning</code> uniquely identifies a single toll stop warning within this registry
     and is used to retrieve its full metadata.</p></dd>
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-navigation-tollstop" title="class in com.here.sdk.navigation"><code>TollStop</code></a> object associated with the provided <code>warning</code>,
     or <code>null</code> if no warning exists for the given <code>warning</code>.
     This object contains the full details and attributes of the corresponding warning.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getDangerZoneWarning(com.here.sdk.warner.Warning)">
<h3>getDangerZoneWarning</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-dangerzonewarning" title="class in com.here.sdk.navigation">DangerZoneWarning</a></span> <span className="element-name">getDangerZoneWarning</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span></div>
<div className="block"><p>Returns a danger zone warning corresponding to the given identifier.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>warning</code> - <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
     The <code>warning</code> uniquely identifies a single danger zone warning within this registry
     and is used to retrieve its full metadata.</p></dd>
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-navigation-dangerzonewarning" title="class in com.here.sdk.navigation"><code>DangerZoneWarning</code></a> object associated with the provided <code>warning</code>,
     or <code>null</code> if no warning exists for the given <code>warning</code>.
     This object contains the full details and attributes of the corresponding warning.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getBorderCrossingWarning(com.here.sdk.warner.Warning)">
<h3>getBorderCrossingWarning</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarning" title="class in com.here.sdk.navigation">BorderCrossingWarning</a></span> <span className="element-name">getBorderCrossingWarning</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span></div>
<div className="block"><p>Returns a border crossing warning corresponding to the given identifier.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>warning</code> - <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
     The <code>warning</code> uniquely identifies a single border crossing warning within this registry
     and is used to retrieve its full metadata.</p></dd>
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarning" title="class in com.here.sdk.navigation"><code>BorderCrossingWarning</code></a> object associated with the provided <code>warning</code>,
     or <code>null</code> if no warning exists for the given <code>warning</code>.
     This object contains the full details and attributes of the corresponding warning.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRailwayCrossingWarning(com.here.sdk.warner.Warning)">
<h3>getRailwayCrossingWarning</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-railwaycrossingwarning" title="class in com.here.sdk.navigation">RailwayCrossingWarning</a></span> <span className="element-name">getRailwayCrossingWarning</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span></div>
<div className="block"><p>Returns a railway crossing warning corresponding to the given identifier.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>warning</code> - <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
     The <code>warning</code> uniquely identifies a single railway crossing warning within this registry
     and is used to retrieve its full metadata.</p></dd>
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-navigation-railwaycrossingwarning" title="class in com.here.sdk.navigation"><code>RailwayCrossingWarning</code></a> object associated with the provided <code>warning</code>,
     or <code>null</code> if no warning exists for the given <code>warning</code>.
     This object contains the full details and attributes of the corresponding warning.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getLowSpeedZoneWarning(com.here.sdk.warner.Warning)">
<h3>getLowSpeedZoneWarning</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-lowspeedzonewarning" title="class in com.here.sdk.navigation">LowSpeedZoneWarning</a></span> <span className="element-name">getLowSpeedZoneWarning</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span></div>
<div className="block"><p>Returns a low speed zone warning corresponding to the given identifier.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>warning</code> - <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
     The <code>warning</code> uniquely identifies a single low speed zone warning within this registry
     and is used to retrieve its full metadata.</p></dd>
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-navigation-lowspeedzonewarning" title="class in com.here.sdk.navigation"><code>LowSpeedZoneWarning</code></a> object associated with the provided <code>warning</code>,
     or <code>null</code> if no warning exists for the given <code>warning</code>.
     This object contains the full details and attributes of the corresponding warning.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTrafficMergeWarning(com.here.sdk.warner.Warning)">
<h3>getTrafficMergeWarning</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarning" title="class in com.here.sdk.navigation">TrafficMergeWarning</a></span> <span className="element-name">getTrafficMergeWarning</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span></div>
<div className="block"><p>Returns a traffic merge warning corresponding to the given identifier.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>warning</code> - <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
     The <code>warning</code> uniquely identifies a single traffic merge warning within this registry
     and is used to retrieve its full metadata.</p></dd>
<dt>Returns:</dt>
<dd><p>The <code>sdk.navigation.TrafficMergeWarning</code> object associated with the provided <code>warning</code>,
     or <code>null</code> if no warning exists for the given <code>warning</code>.
     This object contains the full details and attributes of the corresponding warning.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getLaneDecreaseWarning(com.here.sdk.warner.Warning)">
<h3>getLaneDecreaseWarning</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-warner-lanedecreasewarning" title="class in com.here.sdk.warner">LaneDecreaseWarning</a></span> <span className="element-name">getLaneDecreaseWarning</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span></div>
<div className="block"><p>Returns a lane decrease warning corresponding to the given identifier.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>warning</code> - <p>The identifier of the warning, as provided by <code>WarningListener.onWarning</code>.
     The <code>warning</code> uniquely identifies a single lane decrease warning within this registry
     and is used to retrieve its full metadata.</p></dd>
<dt>Returns:</dt>
<dd><p>The <code>LaneDecreaseWarning</code> object associated with the provided <code>warning</code>,
     or <code>null</code> if no warning exists for the given <code>warning</code>.
     This object contains the full details and attributes of the corresponding warning.
     <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
     behaviors. Related APIs may change for new releases without a deprecation process.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getCustomWarning(com.here.sdk.warner.Warning)">
<h3>getCustomWarning</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-warner-customwarning" title="class in com.here.sdk.warner">CustomWarning</a></span> <span className="element-name">getCustomWarning</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span></div>
<div className="block"><p>Returns additional data associated with the given custom warning.
 The provided <code>warning</code> identifies a specific custom warning instance by its
 base warning information and custom warning type. This information is used
 to resolve the corresponding entry in the warning registry and retrieve
 any additional, type-specific data associated with the warning.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>warning</code> - <p>The <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner"><code>Warning</code></a> instance identifying the custom warning for which
     additional data should be retrieved.</p></dd>
<dt>Returns:</dt>
<dd><p>The <code>CustomWarning</code> associated with the given <code>warning</code>, or <code>null</code>
     if no additional data exists for this warning.
     The returned object contains the payload with type-specific
     details and attributes of the corresponding warning.
     <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
     behaviors. Related APIs may change for new releases without a deprecation process.</p></dd>
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
