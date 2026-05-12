---
title: "com.here.sdk.trafficbroadcast (API Reference)"
slug: "sdk-for-android-navigate-navigate-com-here-sdk-trafficbroadcast-package-summary"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- package-summary.html -->
<!DOCTYPE HTML>

<html lang="en">

<body class="package-declaration-page">


<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-navigate-index">Overview</a></li>
<li class="nav-bar-cell1-rev">Package</li>
<li>Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-help-doc#package">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Package: </li>
<li>Description | </li>
<li>Related Packages | </li>
<li><a href="#class-summary">Classes and Interfaces</a></li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<div class="header">

</div>
<hr/>
<div class="package-signature">package <span class="element-name">com.here.sdk.trafficbroadcast</span></div>
<section class="summary">
<ul class="summary-list">
<li>
<div id="class-summary">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="class-summary.tabpanel" aria-selected="true" class="active-table-tab" id="class-summary-tab0" onclick="show('class-summary', 'class-summary', 2)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Classes and Interfaces</button><button aria-controls="class-summary.tabpanel" aria-selected="false" class="table-tab" id="class-summary-tab1" onclick="show('class-summary', 'class-summary-tab1', 2)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Interfaces</button><button aria-controls="class-summary.tabpanel" aria-selected="false" class="table-tab" id="class-summary-tab2" onclick="show('class-summary', 'class-summary-tab2', 2)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Classes</button></div>
<div aria-labelledby="class-summary-tab0" id="class-summary.tabpanel" role="tabpanel">
<div class="summary-table two-column-summary">
<div class="table-header col-first">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-rdsencryptionkey" title="class in com.here.sdk.trafficbroadcast">RDSEncryptionKey</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Represents the RDS encryption key.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-rdsencryptionkeysrequest" title="class in com.here.sdk.trafficbroadcast">RDSEncryptionKeysRequest</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Represents data to search for RDS encryption keys.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-tmcdata" title="class in com.here.sdk.trafficbroadcast">TMCData</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Represents the traffic events in RDS-TMC format.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-tmcpreferredsidsrequest" title="class in com.here.sdk.trafficbroadcast">TMCPreferredSidsRequest</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Represents data used to request the list of preferred SIDs.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab1"><a href="sdk-for-android-navigate-tmcserviceinterface" title="interface in com.here.sdk.trafficbroadcast">TMCServiceInterface</a></div>
<div class="col-last even-row-color class-summary class-summary-tab1">
<div class="block">Contains all outgoing dependencies to the client side.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-tmcserviceproviderinfo" title="class in com.here.sdk.trafficbroadcast">TMCServiceProviderInfo</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Represents the service prodiver info in RDS-TMC format.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-tmcservicerequest" title="class in com.here.sdk.trafficbroadcast">TMCServiceRequest</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Represents the parameters used to request the traffic broadcast.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-trafficbroadcast" title="class in com.here.sdk.trafficbroadcast">TrafficBroadcast</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">A <code>TrafficBroadcast</code> is expecting the <a href="https://en.wikipedia.org/wiki/Traffic_message_channel">RDS-TMC</a>
 format and it can be used when there is no internet connection, so that the <code>OfflineRoutingEngine</code>
 can utilize traffic data coming over a radio channel.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-trafficbroadcastparameters" title="class in com.here.sdk.trafficbroadcast">TrafficBroadcastParameters</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Represents the parameters needed to request the traffic broadcast.</div>
</div>
</div>
</div>
</div>
</li>
</ul>
</section>
</main>
</div>
</div>
</body>
</html>

</div>
`
}</HTMLBlock>
