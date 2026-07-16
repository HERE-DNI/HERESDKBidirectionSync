---
title: "CatalogUpdateProgressListener Protocol Reference"
slug: "sdk-for-ios-navigate-protocols-catalogupdateprogresslistener"
---

# CatalogUpdateProgressListener

<div class="declaration">

<div class="language">

``` highlight
public protocol CatalogUpdateProgressListener : AnyObject
```

</div>

</div>

Protocol to get notified on status updates when updating catalog, previously downloaded by <a href="sdk-for-ios-navigate-classes-mapdownloader">`MapDownloader`</a>.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk29CatalogUpdateProgressListenerP02onD06region10percentageyAA8RegionIdV_s5Int32VtF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-onProgress-region-percentage" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-protocols-catalogupdateprogresslistener#sdk-for-ios-navigate-s-7heresdk29CatalogUpdateProgressListenerP02onD06region10percentageyAA8RegionIdV_s5Int32VtF" class="token"><code>onProgress(region:</code><wbr></wbr><code>percentage:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called multiple times to indicate the update progress. Invoked on the main thread.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func onProgress(region: RegionId, percentage: Int32)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-regionid">RegionId</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>region</code></em><code> </code></td>
  <td><div>
  <p>Represents an id of region status update is related to.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>percentage</code></em><code> </code></td>
  <td><div>
  <p>Represents a percentage of catalog data which has been updated.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk29CatalogUpdateProgressListenerP7onPause5erroryAA14MapLoaderErrorOSg_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-onPause-error" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-protocols-catalogupdateprogresslistener#sdk-for-ios-navigate-s-7heresdk29CatalogUpdateProgressListenerP7onPause5erroryAA14MapLoaderErrorOSg_tF" class="token"><code>onPause(error:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called when update is paused. Invoked on the main thread.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func onPause(error: MapLoaderError?)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-maploadererror">MapLoaderError</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>error</code></em><code> </code></td>
  <td><div>
  <p>Populated when a retryable error is the reason for a pause. A retryable error can happen, when, for example, the HERE SDK tries too often to resume a download that was paused due to a lost connection. In general, the HERE SDK will try a few times, before the update is paused. This error value gives a hint on the reason for the necessary retry operation. A paused download can be resumed by the user at a later time. It is ‘null’ when</p>
  <pre><code>CatalogUpdateTask.pause(Bool)</code></pre>
  was called by the user.
  </p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk29CatalogUpdateProgressListenerP10onComplete5erroryAA14MapLoaderErrorOSg_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-onComplete-error" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-protocols-catalogupdateprogresslistener#sdk-for-ios-navigate-s-7heresdk29CatalogUpdateProgressListenerP10onComplete5erroryAA14MapLoaderErrorOSg_tF" class="token"><code>onComplete(error:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called after the update process for all regions has been completed. Invoked on the main thread.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func onComplete(error: MapLoaderError?)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-maploadererror">MapLoaderError</a>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>error</code></em><code> </code></td>
  <td><div>
  <p>Represents an error in case of a failure. If an error occurs, the operation cannot be resumed later. It is <code>nil</code> for an operation that succeeds.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk29CatalogUpdateProgressListenerP8onResumeyyF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-onResume" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-protocols-catalogupdateprogresslistener#sdk-for-ios-navigate-s-7heresdk29CatalogUpdateProgressListenerP8onResumeyyF" class="token"><code>onResume()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called when a paused map update is resumed.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func onResume()
  ```

  </div>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

