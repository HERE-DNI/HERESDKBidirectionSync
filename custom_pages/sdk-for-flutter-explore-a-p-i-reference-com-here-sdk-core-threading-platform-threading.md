---
title: "Platform Threading"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-platform-threading"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.core.threading/PlatformThreading///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading/PlatformThreading</div>
<div class="cover">
<h1 class="cover">Platform<wbr/>Threading</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">interface /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-platform-threading</div><p class="paragraph">Interface for task activities on the main thread.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="postToMainThread" data-filterable-set=":modules:dokkaHtml/release" data-name="-2051789102%2FFunctions%2F1617540583" id="-2051789102%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-platform-threading-post-to-main-thread</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">abstract fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-platform-threading-post-to-main-thread(runnable: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-runnable): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Posts task to the end of the queue of the main thread. Function does not wait for task to be executed and returns immediately after the task is put to the queue. Note: Depending on actual platform, destruction-time of passed in runnable might be unknown due to unpredictability of garbage collection. Therefore, runnable should not hold strong references to objects whose lifetimes are critical or references should be released at the end of execution.</p></div><div class="symbol monospace">abstract fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-platform-threading-post-to-main-thread(runnable: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-runnable, delayMs: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html">Long</a>): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Posts a task to be executed on the main thread after some delay. If the delay is 0, the function puts the task at the end of the queue. The function does not wait for the task to be executed and returns immediately after the task has been put in the queue. Note: Depending on actual platform, destruction-time of passed in runnable might be unknown due to unpredictability of garbage collection. Therefore, runnable should not hold strong references to objects whose lifetimes are critical or references should be released at the end of execution.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="runOnMainThread" data-filterable-set=":modules:dokkaHtml/release" data-name="-66630082%2FFunctions%2F1617540583" id="-66630082%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-platform-threading-run-on-main-thread</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">abstract fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-platform-threading-run-on-main-thread(runnable: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-runnable): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-threading-task-handle</div><div class="brief"><p class="paragraph">Runs a task on the main thread. If this function is called from the main thread, then the task will run immediately. Otherwise, it is put to the end of the queue of the main thread. Note: Depending on actual platform, destruction-time of passed in runnable might be unknown due to unpredictability of garbage collection. Therefore, runnable should not hold strong references to objects whose lifetimes are critical or references should be released at the end of execution.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="footer">
<a class="footer--button footer--button_go-to-top" href="#content" id="go-to-top-link"></a>
© 2026 Copyright

Generated by 
<a class="footer--link footer--link_external" href="https://github.com/Kotlin/dokka">
dokka
</a>

</div>
</div>

</div>

</div>
`
}</HTMLBlock>
