---
title: "RouteDeviationListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-routedeviationlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- RouteDeviationListener.html -->






<div class="flex-box">

<div class="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">RouteDeviationListener</span></div>
<div class="block"><p>This interface should be implemented in order to
 receive notifications
 about route deviations from <a href="sdk-for-android-navigate-com-here-sdk-navigation-navigator" title="class in com.here.sdk.navigation"><code>Navigator</code></a>.</p></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-navigation-routedeviationlistener#onRouteDeviation(com.here.sdk.navigation.RouteDeviation)">onRouteDeviation</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-navigation-routedeviation" title="class in com.here.sdk.navigation">RouteDeviation</a> routeDeviation)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called whenever route deviation has been observed.</div>
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
<section class="detail" id="onRouteDeviation(com.here.sdk.navigation.RouteDeviation)">
<h3>onRouteDeviation</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onRouteDeviation</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-routedeviation" title="class in com.here.sdk.navigation">RouteDeviation</a> routeDeviation)</span></div>
<div class="block"><p>Called whenever route deviation has been observed. It contains the information
 that can be used to decide whether to request a re-route calculation from the routing engine.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>routeDeviation</code> - <p>The route deviation observed.</p></dd>
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
