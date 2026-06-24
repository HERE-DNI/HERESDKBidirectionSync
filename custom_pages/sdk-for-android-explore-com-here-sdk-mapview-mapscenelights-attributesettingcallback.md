---
title: "MapSceneLights.AttributeSettingCallback (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapscenelights-attributesettingcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapSceneLights.AttributeSettingCallback.html -->










<!-- ======== START OF CLASS DATA ======== -->

<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-explore-mapscenelights" title="class in com.here.sdk.mapview">MapSceneLights</a></dd>
</dl>
<dl class="notes">
<dt>Functional Interface:</dt>
<dd>This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.</dd>
</dl>

<div class="type-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public static interface </span><span class="element-name type-name-label">MapSceneLights.AttributeSettingCallback</span></div>
<div class="block"><p>This callback function allows handling errors that occur during the setting of light attributes.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapscenelights-attributesettingcallback#onAttributeSetting(com.here.sdk.mapview.MapSceneLights.AttributeSettingError)">onAttributeSetting</a><wbr/>(<a href="sdk-for-android-explore-mapscenelights.attributesettingerror" title="enum class in com.here.sdk.mapview">MapSceneLights.AttributeSettingError</a> setLightError)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">This callback function allows handling errors that occur during the setting of light attributes.</div>
</div>
</div>
</div>
</div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="onAttributeSetting(com.here.sdk.mapview.MapSceneLights.AttributeSettingError)">
<h3>onAttributeSetting</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onAttributeSetting</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-explore-mapscenelights.attributesettingerror" title="enum class in com.here.sdk.mapview">MapSceneLights.AttributeSettingError</a> setLightError)</span></div>
<div class="block"><p>This callback function allows handling errors that occur during the setting of light attributes.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>setLightError</code> - <p>The cause for the failure when setting the light attributes, or <code>null</code> if no error occurred.
     </p><p>Note: The error code <code>NO_LIGHTS</code> may be returned when attempting to set light attributes in map schemes
     that do not support lights, for instance <code>road.network</code> map scheme.
     </p><p>Please refer to the error code documentation for further details on error handling.</p></dd>
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
