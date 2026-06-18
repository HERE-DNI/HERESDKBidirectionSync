---
title: "com.here.sdk.location (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-location-package-summary"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- package-summary.html -->









<main role="main">
<div class="header">

</div>
<hr/>
<div class="package-signature">package <span class="element-name">com.here.sdk.location</span></div>
<section class="summary">
<ul class="summary-list">
<li>
<div id="class-summary">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="class-summary.tabpanel" aria-selected="true" class="active-table-tab" id="class-summary-tab0" onclick="show('class-summary', 'class-summary', 2)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Classes and Interfaces</button><button aria-controls="class-summary.tabpanel" aria-selected="false" class="table-tab" id="class-summary-tab1" onclick="show('class-summary', 'class-summary-tab1', 2)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Interfaces</button><button aria-controls="class-summary.tabpanel" aria-selected="false" class="table-tab" id="class-summary-tab2" onclick="show('class-summary', 'class-summary-tab2', 2)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Classes</button><button aria-controls="class-summary.tabpanel" aria-selected="false" class="table-tab" id="class-summary-tab3" onclick="show('class-summary', 'class-summary-tab3', 2)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Enum Classes</button></div>
<div aria-labelledby="class-summary-tab0" id="class-summary.tabpanel" role="tabpanel">
<div class="summary-table two-column-summary">
<div class="table-header col-first">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-cellularpositioningoptions" title="class in com.here.sdk.location">CellularPositioningOptions</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Cellular positioning options.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-navigate-confirmationstatus" title="enum class in com.here.sdk.location">ConfirmationStatus</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Confirmation action specific status codes.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-navigate-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Indicates the desired location accuracy, however the actual accuracy is not
 guaranteed.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-locationengine" title="class in com.here.sdk.location">LocationEngine</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">This class handles location updates received according to the desired <a href="sdk-for-android-navigate-locationaccuracy" title="enum class in com.here.sdk.location"><code>LocationAccuracy</code></a> or <a href="sdk-for-android-navigate-locationoptions" title="class in com.here.sdk.location"><code>LocationOptions</code></a>.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab1"><a href="sdk-for-android-navigate-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></div>
<div class="col-last even-row-color class-summary class-summary-tab1">
<div class="block">Public interface that describes the behaviour of <code>LocationEngine</code>.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-navigate-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Indicates the status of the LocationEngine.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-navigate-locationfeature" title="enum class in com.here.sdk.location">LocationFeature</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Location features supported by HERE positioning.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab1"><a href="sdk-for-android-navigate-locationissuelistener" title="interface in com.here.sdk.location">LocationIssueListener</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab1">
<div class="block">interface receiving notifications when the set of
 currently active location issues changes.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-navigate-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Represents specific issues affecting location retrieval quality, availability, or functionality.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-locationoptions" title="class in com.here.sdk.location">LocationOptions</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Location options that combine notification, sensor, cellular positioning, GNSS positioning and WiFi positioning options.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab1"><a href="sdk-for-android-navigate-locationstatuslistener" title="interface in com.here.sdk.location">LocationStatusListener</a></div>
<div class="col-last even-row-color class-summary class-summary-tab1">
<div class="block">Interface for listening the
 LocationEngine status updates.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-notificationoptions" title="class in com.here.sdk.location">NotificationOptions</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Positioning notification options.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-satellitepositioningoptions" title="class in com.here.sdk.location">SatellitePositioningOptions</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">GNSS positioning options.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-sensoroptions" title="class in com.here.sdk.location">SensorOptions</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Options for controlling sensor usage in positioning.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-wifipositioningoptions" title="class in com.here.sdk.location">WifiPositioningOptions</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Wi-Fi positioning options.</div>
</div>
</div>
</div>
</div>
</li>
</ul>
</section>
</main>





</div>
`
}</HTMLBlock>
