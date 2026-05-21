---
title: "destroy Locking Process"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-locking-process-companion-destroy-locking-process"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- destroy-locking-process.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="member" id="content" pageids="API Reference::com.here.sdk.core.engine/LockingProcess.Companion/destroyLockingProcess/#android.content.Context#com.here.sdk.core.engine.SDKOptions#kotlin.Long/PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-locking-process//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-locking-process-companion/destroyLockingProcess</div>
<div class="cover">
<h1 class="cover">destroy<wbr/>Locking<wbr/>Process</h1>
</div>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html">JvmStatic</a></div></div>external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-locking-process-companion-destroy-locking-process(context: <a href="https://developer.android.com/reference/kotlin/android/content/Context.html">Context</a>, sdkOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-s-d-k-options, maxTimeoutInMilliseconds: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html">Long</a>)</div><p class="paragraph">Checks if cache folder is locked. Does nothing if cache is not locked or locked by current process. If cache is locked by a different process then the HERE SDK makes a few attempts to kill the locking application during the specified timeout. If it fails to kill the application, it attempts to remove the cache at /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-s-d-k-options-cache-path. This function can be used before creating a SDKNativeEngine, i.e.</p><pre>
{@code
    SDKOptions options = new SDKOptions(...);
    LockingProcess.destroyLockingProcess(context, options, 300);
    SDKNativeEngine engine = new SDKNativeEngine(options);
}
</pre><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>context</u></div></div><div><div class="title"><p class="paragraph">The Android context</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>sdk<wbr/>Options</u></div></div><div><div class="title"><p class="paragraph">The options which are supposed to be used for a new instance of the engine.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>max<wbr/>Timeout<wbr/>In<wbr/>Milliseconds</u></div></div><div><div class="title"><p class="paragraph">The maximum timeout in milliseconds. Recommended value is 300 - 500 milliseconds.     If 0 or a negative value is passed then it makes only one attempt to kill the locking     process (if any) and waits 30 milliseconds before exit because the system may spend a     small amount of time to perform the operation.</p></div></div></div></div></div><hr/><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-static/index.html">JvmStatic</a></div></div>external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-locking-process-companion-destroy-locking-process(sdkOptions: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-s-d-k-options, maxTimeoutInMilliseconds: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html">Long</a>)</div><div class="deprecation-content"><h3 class="">Deprecated</h3><p class="paragraph">Will be removed in v4.27.0, use [com.here.sdk.core.engine.LockingProcess.destroyLockingProcess] instead.</p></div><p class="paragraph">Checks if cache folder is locked. Does nothing if cache is not locked or locked by current process. If cache is locked by a different process then the HERE SDK makes a few attempts to kill the locking application during the specified timeout. If it fails to kill the application, it attempts to remove the cache at /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-engine-s-d-k-options-cache-path. This function can be used before creating a SDKNativeEngine, i.e.</p><pre>
{@code
    SDKOptions options = new SDKOptions(...);
    LockingProcess.destroyLockingProcess(options, 300);
    SDKNativeEngine engine = new SDKNativeEngine(options);
}
</pre><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>sdk<wbr/>Options</u></div></div><div><div class="title"><p class="paragraph">The options which are supposed to be used for a new instance of the engine.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>max<wbr/>Timeout<wbr/>In<wbr/>Milliseconds</u></div></div><div><div class="title"><p class="paragraph">The maximum timeout in milliseconds. Recommended value is 300 - 500 milliseconds.     If 0 or a negative value is passed then it makes only one attempt to kill the locking     process (if any) and waits 30 milliseconds before exit because the system may spend a     small amount of time to perform the operation.</p></div></div></div></div></div></div></div>
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
