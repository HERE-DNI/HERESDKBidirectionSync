---
title: "OfflineSearchIndexListener Protocol Reference"
slug: "sdk-for-ios-explore-protocols-offlinesearchindexlistener"
---

# OfflineSearchIndexListener

<div class="declaration">

<div class="language">

``` highlight
public protocol OfflineSearchIndexListener : AnyObject
```

</div>

</div>

Protocol to get updates about progress of creating persistent map index.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk26OfflineSearchIndexListenerP9onStarted9operationyAA0bcD0C9OperationO_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-onStarted-operation" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-offlinesearchindexlistener#sdk-for-ios-explore-s-7heresdk26OfflineSearchIndexListenerP9onStarted9operationyAA0bcD0C9OperationO_tF" class="token"><code>onStarted(operation:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called each time that the indexing has started. It is triggered by changes to persistent map or by calling `OfflineSearchEngine.setIndexOptions`. If a valid index was previously created for the installed regions, no additional indexing is performed, so no notifications are sent. In this context, a valid index is the one that contains data for the exact versions of the installed map regions. When any of them is updated or new regions are downloaded or deleted, the index becomes invalid and is automatically rebuilt, as long as indexing has been enabled previously. Invoked on the main thread.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func onStarted(operation: OfflineSearchIndex.Operation)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-offlinesearchindex">OfflineSearchIndex</a>

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
  <td><code> </code><em><code>operation</code></em><code> </code></td>
  <td><div>
  <p>Shows whether the index is being created or removed.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk26OfflineSearchIndexListenerP10onProgress10percentageys5Int32V_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-onProgress-percentage" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-offlinesearchindexlistener#sdk-for-ios-explore-s-7heresdk26OfflineSearchIndexListenerP10onProgress10percentageys5Int32V_tF" class="token"><code>onProgress(percentage:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called multiple times to indicate the progress of index creation or deletion. Invoked on the main thread.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func onProgress(percentage: Int32)
  ```

  </div>

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
  <td><code> </code><em><code>percentage</code></em><code> </code></td>
  <td><div>
  <p>Represents a percentage of work done.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk26OfflineSearchIndexListenerP10onComplete5erroryAA0bcD0C5ErrorOSg_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-onComplete-error" class="dashAnchor"></span> <a href="sdk-for-ios-explore-protocols-offlinesearchindexlistener#sdk-for-ios-explore-s-7heresdk26OfflineSearchIndexListenerP10onComplete5erroryAA0bcD0C5ErrorOSg_tF" class="token"><code>onComplete(error:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Called after index creation or deletion has been completed. Invoked on the main thread.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  func onComplete(error: OfflineSearchIndex.Error?)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-offlinesearchindex">OfflineSearchIndex</a>

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
  <p>Represents an error in case of a failure. It is <code>nil</code> for an operation that succeeds.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

