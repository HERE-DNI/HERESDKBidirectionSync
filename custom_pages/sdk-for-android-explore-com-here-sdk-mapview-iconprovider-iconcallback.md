---
title: "IconProvider.IconCallback (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-iconprovider-iconcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- IconProvider.IconCallback.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-package-summary">com.here.sdk.mapview</a></div>

</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-iconprovider" title="class in com.here.sdk.mapview">IconProvider</a></dd>
</dl>
<dl class="notes">
<dt>Functional Interface:</dt>
<dd>This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.</dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public static interface </span><span class="element-name type-name-label">IconProvider.IconCallback</span></div>
<div class="block">Interface which is used as callback to pass back an image or error code after calling
 the createRoadShieldIcon() method.</div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-index#onCreateIconReply(android.graphics.Bitmap,java.lang.String,com.here.sdk.mapview.IconProviderError)">onCreateIconReply</a><wbr/>(android.graphics.Bitmap bitmap,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-iconprovidererror" title="enum class in com.here.sdk.mapview">IconProviderError</a> error)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called when the image was created successfully or an error has occurred</div>
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
<section class="detail" id="onCreateIconReply(android.graphics.Bitmap,java.lang.String,com.here.sdk.mapview.IconProviderError)">
<h3>onCreateIconReply</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onCreateIconReply</span><wbr/><span class="parameters">(@Nullable
 android.graphics.Bitmap bitmap,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> description,
 @Nullable
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-explore-iconprovidererror" title="enum class in com.here.sdk.mapview">IconProviderError</a> error)</span></div>
<div class="block">Called when the image was created successfully or an error has occurred</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>bitmap</code> - The created icon or <code>null</code> if an error occurred. Note that the
               resulting resolution of the image may differ from the width and height
               constraints because the aspect ratio is kept.</dd>
<dd><code>description</code> - An English description of the created icon. For example,
                    "Federal Highway" for the road shield icon with the
                    <code>RouteType.LEVEL_1_ROAD</code> in Brazil.
                    Empty string if an error occurred.</dd>
<dd><code>error</code> - Error code if icon creation failed.</dd>
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
