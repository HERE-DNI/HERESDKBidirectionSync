---
title: "ScooterSpecification Structure Reference"
slug: "sdk-for-ios-navigate-structs-scooterspecification"
---

# ScooterSpecification

<div class="declaration">

<div class="language">

``` highlight
public struct ScooterSpecification : Hashable
```

</div>

</div>

Scooter specific settings.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20ScooterSpecificationV05allowB9OnHighwaySbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-allowScooterOnHighway" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-scooterspecification#sdk-for-ios-navigate-s-7heresdk20ScooterSpecificationV05allowB9OnHighwaySbvp" class="token"><code>allowScooterOnHighway</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies whether scooter is allowed on highway or not. `True` means scooter is allowed to use highways and `false` means otherwise. Defaults to `false`. Note that there is a similar parameter in <a href="sdk-for-ios-navigate-structs-avoidanceoptions">`AvoidanceOptions`</a>, to disallow highway usage, see `RoadFeatures.CONTROLLED_ACCESS_HIGHWAY`. As the avoidance options takes precedence, if this parameter is also used, then scooters are not allowed to use highways even if `allowHighway` is set to `true`. However, if no alternative route is possible, the calculated route may use highways. In such a case, a <a href="sdk-for-ios-navigate-structs-sectionnotice">`SectionNotice`</a> will be provided in the related <a href="sdk-for-ios-navigate-classes-section">`Section`</a> to indicate that the highway usage restriction is violated on this route. A few examples:

  1 - If no avoidance option is set, and `allowHighway = false`, when no route is found without highway usage, a notice is received.

  2 - If no avoidance option is set, and `allowHighway = true`, when no route is found without highway usage, no notice is received.

  3 - If only `avoid[features] = controlledAccessHighway` is set, when no route is found without highway usage, a notice is received.

  4 - If both `avoid[features] = controlledAccessHighway` and `allowHighway = true` are set, when no route is found without highway usage, a notice is received.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var allowScooterOnHighway: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20ScooterSpecificationV05allowB9OnHighwayACSb_tcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-allowScooterOnHighway" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-scooterspecification#sdk-for-ios-navigate-s-7heresdk20ScooterSpecificationV05allowB9OnHighwayACSb_tcfc" class="token"><code>init(allowScooterOnHighway:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  - Parameters

    - allowScooterOnHighway: Specifies whether scooter is allowed on highway or not. `True` means scooter is allowed to use highways and `false` means otherwise. Defaults to `false`. Note that there is a similar parameter in <a href="sdk-for-ios-navigate-structs-avoidanceoptions">`AvoidanceOptions`</a>, to disallow highway usage, see `RoadFeatures.CONTROLLED_ACCESS_HIGHWAY`. As the avoidance options takes precedence, if this parameter is also used, then scooters are not allowed to use highways even if `allowHighway` is set to `true`. However, if no alternative route is possible, the calculated route may use highways. In such a case, a <a href="sdk-for-ios-navigate-structs-sectionnotice">`SectionNotice`</a> will be provided in the related <a href="sdk-for-ios-navigate-classes-section">`Section`</a> to indicate that the highway usage restriction is violated on this route. A few examples:

    1 - If no avoidance option is set, and `allowHighway = false`, when no route is found without highway usage, a notice is received.

    2 - If no avoidance option is set, and `allowHighway = true`, when no route is found without highway usage, no notice is received.

    3 - If only `avoid[features] = controlledAccessHighway` is set, when no route is found without highway usage, a notice is received.

    4 - If both `avoid[features] = controlledAccessHighway` and `allowHighway = true` are set, when no route is found without highway usage, a notice is received.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(allowScooterOnHighway: Bool = false)
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

