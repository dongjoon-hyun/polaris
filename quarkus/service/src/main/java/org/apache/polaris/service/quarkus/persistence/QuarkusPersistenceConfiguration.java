/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
package org.apache.polaris.service.quarkus.persistence;

import io.smallrye.config.ConfigMapping;
import io.smallrye.config.WithDefault;
import java.util.Set;

@ConfigMapping(prefix = "polaris.persistence")
public interface QuarkusPersistenceConfiguration {

  /**
   * The type of the persistence to use. Must be a registered {@link
   * org.apache.polaris.core.persistence.MetaStoreManagerFactory} identifier.
   */
  String type();

  @WithDefault("in-memory")
  Set<String> autoBootstrapTypes();

  default boolean isAutoBootstrap() {
    return autoBootstrapTypes().contains(type());
  }
}
