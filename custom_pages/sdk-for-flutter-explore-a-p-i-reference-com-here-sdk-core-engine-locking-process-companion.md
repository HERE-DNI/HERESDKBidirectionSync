---
title: "Companion"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-locking-process-companion"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.core.engine/LockingProcess.Companion///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-locking-process/Companion</div>
<div class="cover">
<h1 class="cover">Companion</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-locking-process-companion</div></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="destroyLockingProcess" data-filterable-set=":modules:dokkaHtml/release" data-name="1421179844%2FFunctions%2F1617540583" id="1421179844%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-locking-process-companion-destroy-locking-process</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html">JvmStatic</a></div></div>external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-locking-process-companion-destroy-locking-process(sdkOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-s-d-k-options, maxTimeoutInMilliseconds: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html">Long</a>)</div><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html">JvmStatic</a></div></div>external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-locking-process-companion-destroy-locking-process(context: <a href="https://developer.android.com/reference/kotlin/android/content/Context.html">Context</a>, sdkOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-s-d-k-options, maxTimeoutInMilliseconds: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html">Long</a>)</div><div class="brief"><p class="paragraph">Checks if cache folder is locked. Does nothing if cache is not locked or locked by current process. If cache is locked by a different process then the HERE SDK makes a few attempts to kill the locking application during the specified timeout. If it fails to kill the application, it attempts to remove the cache at /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-s-d-k-options-cache-path. This function can be used before creating a SDKNativeEngine, i.e.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="getLockingProcessId" data-filterable-set=":modules:dokkaHtml/release" data-name="1376458212%2FFunctions%2F1617540583" id="1376458212%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-locking-process-companion-get-locking-process-id</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html">JvmStatic</a></div></div>external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-locking-process-companion-get-locking-process-id(options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-s-d-k-options): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html">JvmStatic</a></div></div>external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-locking-process-companion-get-locking-process-id(context: <a href="https://developer.android.com/reference/kotlin/android/content/Context.html">Context</a>, options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-s-d-k-options): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Gets the process ID (PID) that currently locks the map cache or the persistent map storage. Returns <code class="lang-kotlin">null</code>, when no lock is active. Usually, a lock is not happening on the current process. The PID of the current process can be checked with <code class="lang-kotlin">android.os.Process#myPid()</code>. The PID can be used to kill or to send a signal to the process with the related functions: <code class="lang-kotlin">android.os.Process#killProcess(int)</code> and <code class="lang-kotlin">android.os.Process#sendSignal(int,int)</code>. Note that the PID might belong to the current app process, so it is recommended to check this before a process is killed as otherwise you will kill your own app process. Alternatively, call the convenient function /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-locking-process-companion-destroy-locking-process.</p></div></div></div>
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
