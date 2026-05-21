---
title: "get Locking Process Id"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-locking-process-companion-get-locking-process-id"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- get-locking-process-id.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="member" id="content" pageids="API Reference::com.here.sdk.core.engine/LockingProcess.Companion/getLockingProcessId/#android.content.Context#com.here.sdk.core.engine.SDKOptions/PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-locking-process//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-locking-process-companion/getLockingProcessId</div>
<div class="cover">
<h1 class="cover">get<wbr/>Locking<wbr/>Process<wbr/>Id</h1>
</div>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html">JvmStatic</a></div></div>external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-locking-process-companion-get-locking-process-id(context: <a href="https://developer.android.com/reference/kotlin/android/content/Context.html">Context</a>, options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-s-d-k-options): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><p class="paragraph">Gets the process ID (PID) that currently locks the map cache or the persistent map storage. Returns <code class="lang-kotlin">null</code>, when no lock is active. Usually, a lock is not happening on the current process. The PID of the current process can be checked with <code class="lang-kotlin">android.os.Process#myPid()</code>. The PID can be used to kill or to send a signal to the process with the related functions: <code class="lang-kotlin">android.os.Process#killProcess(int)</code> and <code class="lang-kotlin">android.os.Process#sendSignal(int,int)</code>. Note that the PID might belong to the current app process, so it is recommended to check this before a process is killed as otherwise you will kill your own app process. Alternatively, call the convenient function /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-locking-process-companion-destroy-locking-process.</p><p class="paragraph">If a PID is available it means that there is a lock on either the cache or the persistant map storage and that the HERE SDK will be non-functional until the locking process is killed. In such a case, consider to kill the locking process.</p><p class="paragraph"><strong>Note:</strong> The Operation is not atomic and may return a PID for a process which is already destroyed or the file might be locked by another thread or process after this function returned <code class="lang-kotlin">null</code>.</p><h4 class="">Return</h4><p class="paragraph">Process ID if the cache or the persistent map directory is locked and a process ID was successfully read.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>context</u></div></div><div><div class="title"><p class="paragraph">The Android context</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>options</u></div></div><div><div class="title"><p class="paragraph">The options which are supposed to be used for new instance of the engine.</p></div></div></div></div></div><hr/><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html">JvmStatic</a></div></div>external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-locking-process-companion-get-locking-process-id(options: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-s-d-k-options): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="deprecation-content"><h3 class="">Deprecated</h3><p class="paragraph">Will be removed in v4.27.0, use [com.here.sdk.core.engine.LockingProcess.getLockingProcessId] instead.</p></div><p class="paragraph">Gets the process ID (PID) that currently locks the map cache or the persistent map storage. Returns <code class="lang-kotlin">null</code>, when no lock is active. Usually, a lock is not happening on the current process. The PID of the current process can be checked with <code class="lang-kotlin">android.os.Process#myPid()</code>. The PID can be used to kill or to send a signal to the process with the related functions: <code class="lang-kotlin">android.os.Process#killProcess(int)</code> and <code class="lang-kotlin">android.os.Process#sendSignal(int,int)</code>. Note that the PID might belong to the current app process, so it is recommended to check this before a process is killed as otherwise you will kill your own app process. Alternatively, call the convenient function /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-locking-process-companion-destroy-locking-process.</p><p class="paragraph">If a PID is available it means that there is a lock on either the cache or the persistant map storage and that the HERE SDK will be non-functional until the locking process is killed. In such a case, consider to kill the locking process.</p><p class="paragraph"><strong>Note:</strong> The Operation is not atomic and may return a PID for a process which is already destroyed or the file might be locked by another thread or process after this function returned <code class="lang-kotlin">null</code>.</p><h4 class="">Return</h4><p class="paragraph">Process ID if the cache or the persistent map directory is locked and a process ID was successfully read.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>options</u></div></div><div><div class="title"><p class="paragraph">The options which are supposed to be used for new instance of the engine.</p></div></div></div></div></div></div></div>
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
