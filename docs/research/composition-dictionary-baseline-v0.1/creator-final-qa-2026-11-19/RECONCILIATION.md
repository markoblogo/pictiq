# С01.17 — Final Creator QA v0.2: reconciliation

2026-11-19. Проверен чистый HEAD `af615cc3f6d9c767b6059c6114c4a8d2cff1277f`. Только reconciliation предоставленного экспорта и применений; без новой семантической QA, freeze или проверки deployed-сайта.

```text
CREATOR QA RECONCILIATION: PASS
TIMETABLE APPLICATION: VERIFIED
DICTIONARY FREEZE READINESS: READY
PUBLIC RELEASE READINESS: BLOCKED
BASELINE FREEZE: NOT PERFORMED
```

## Десять решений

**E** — [исходный creator export](creator-export.json); `/records/N` ниже относится именно к нему. **D** — [текущий Dictionary](../dictionary.json). У всех десяти карточек есть допустимое решение: **10/10**, без UNREVIEWED/UNRESOLVED. Распределение: 4 ACCEPT_AS_SHOWN, 4 NEEDS_CORRECTION, 1 KEEP_ENTRY_CHANGE_PREFERRED, 1 MOVE_TO_CORPUS_ONLY.

| ID | Решение автора | Итоговое состояние | Evidence | Статус |
| --- | --- | --- | --- | --- |
| `pcd-v01-0002` | NEEDS_CORRECTION | Уточнены self/указание/другой человек вне общего зрительного контакта или письменно; Messages сохранены. | E `/records/0`; [A1](../applied-decisions/pcd-v01-0002-context.json) | APPLIED |
| `pcd-v01-0005` | ACCEPT_AS_SHOWN | `food_meat`; вся статья сохранена без исправлений, комментарий автора остаётся в E. | E `/records/1`; D по ID | PRESERVED |
| `pcd-v01-0006` | NEEDS_CORRECTION | Две comm_sound-формы уточнены; человеческая коммуникация/звук, локальная LESS/DOWN синонимия. comm_speak не изменён. | E `/records/2`; [A2](../applied-decisions/pcd-v01-0006-context.json) | APPLIED |
| `pcd-v01-0009` | NEEDS_CORRECTION | Уточнены покупки и тип магазина: существующий `place_shop + need_food`; новые специализированные формы не созданы. | E `/records/3`; [A3](../applied-decisions/pcd-v01-0009-context.json) | APPLIED |
| `pcd-v01-0010` | ACCEPT_AS_SHOWN | Обе пищевые LESS/DOWN формы и статья сохранены; контекстные прочтения автора сохранены в E. | E `/records/4`; D по ID | PRESERVED |
| `pcd-v01-0025` | MOVE_TO_CORPUS_ONLY, locked | Из D исключена; HERE + NO сохранено в Corpus `clh-v01-0044`, без замены. Locked-комментарий остаётся пустым. | E `/records/5`; [A6](../applied-decisions/pcd-v01-0025-corpus-only.json); [addendum](../final-creator-qa-addendum-v0.2.json) `/decisions/0` | APPLIED / LOCKED PRESERVED |
| `pcd-v01-0027` | ACCEPT_AS_SHOWN | `move_feet + logic_no`; вся статья сохранена, PERSON не добавлен. | E `/records/6`; D по ID | PRESERVED |
| `pcd-v01-0028` | KEEP_ENTRY_CHANGE_PREFERRED | `move_feet` — preferred только для дорожного знака/WAYFINDING. Также CURRENT_ACCEPTED: `person_generic + move_feet` и `person_generic + move_feet + rel_here`, с отдельным контекстом/provenance. | E `/records/7`; [A5](../applied-decisions/pcd-v01-0028-preferred.json) | APPLIED |
| `pcd-v01-0030` | NEEDS_CORRECTION | Письменное/ситуационное употребление и локальная равнозначность AUTO/NO описаны; парковка не объявлена единственным прочтением. Message сохранён. | E `/records/8`; [A4](../applied-decisions/pcd-v01-0030-context.json) | APPLIED |
| `pcd-v01-0065` | ACCEPT_AS_SHOWN, locked | Arrival-time статья целиком сохранена. Добавление 0066 отдельно; пустой locked-комментарий не дополнен. | E `/records/9`; addendum `/decisions/1/clarification`; [A7](../applied-decisions/pcd-v01-0066-timetable.json) для отдельной статьи | PRESERVED / LOCKED PRESERVED |

Все четыре ACCEPT_AS_SHOWN статьи целиком неизменны относительно исходного Dictionary. Семь применений — четыре уточнения, preferred, исключение и timetable; принятие без правки не требует отдельного application record.

## Timetable и реальные данные

**VERIFIED:** [A7](../applied-decisions/pcd-v01-0066-timetable.json) применяет объект addendum с устойчивым `temporary_qa_id = qa-new-public-transport-timetable`; фактический selector `/decisions/1/new_related_entry`. Одобрение четырёх токенов находится в этом объекте, а не выводится из пустого locked-комментария 0065.

| Статья | Точный Message / token_sequence |
| --- | --- |
| `0065` — When does public transport arrive? | `move_public + time + punct_question` |
| `0066` — Public transport schedule / timetable | `move_public + media_text + time + punct_question` |

Новый [canonical SVG](../renders/pcd-v01-0066-preferred.svg) совпадает с исправленным [K01/K01a preview](../review/previews/qa-new-public-transport-timetable.svg), SHA-256 `b296064c6a9dd5bbdc4df29b88c2c9eb5a554293d0f4f51cac7b1a54ca78b6f2`. [Техническая история K01a](../repairs/K01-timetable-media-text/K01a-REPORT.md) сохранена. Corpus lineage — [clh-v01-0022](../../composition-library-baseline-v0.1/accepted-corpus.json), `/records/21`: его исходный Message остаётся трёхтокенным. У addendum нет собственных mode/surface/context: A7 привязывает унаследованную Corpus applicability `STANDALONE / BOOK`. Это не доказательство публикации четырёхтокенного Message в Handbook.

**65 уникальных entries, 72 уникальных variants**, один PREFERRED на статью. [variants.json](../variants.json) точно соответствует D. Все 72 Messages проходят `schema_errors`/`semantic_errors`; все 72 SVG совпадают с canonical Renderer. Формальная Dictionary JSON Schema отсутствует.

По сравнению с исходным до-QA состоянием: IDs = прежние 65 минус 0025 плюс 0066. Variant IDs = прежние 70 минус `0025-preferred`, плюс два новых варианта 0028 и `0066-preferred`. Все **69 сохранённых прежних variant Messages** неизменны; неожиданных потерь/новых IDs нет. Walking/crossing граница 0028 и условия дорожного preferred сохранены. Corpus 0025/HERE + NO и все исторические SVG остаются доступными.

## Provenance и проверки

Все семь records APPLIED. `verify_sequence` проверил каждый точный обратный delta; полные hashes сохранены в records. Цепочка префиксов:

```text
9c0ed9e048b9 → dccfa377a630 → fea29c8aa2d1 → 9b4bddcb3cff
→ 13b868cc4abc → fe50cf5f62c9 → 4679738d0d2e → b640ec220cee
```

Текущий D SHA-256: `b640ec220ceed0f4f7111791170d0d2f97389c29c8a4306ae6927fbf01c4cdeb`. Все **24 artifact hashes** [manifest](../manifest.json) согласованы. Исторические selectors не переписаны: например A5 `/entries/27` относится к своей исходной версии, тогда как текущая 0028 находится в `/entries/26`.

Исходный E: **13 247 байт**, SHA-256 `609c38175864d5da66e9f969364ea5dc84f71a15eab7bf4cfed14d81d1412152`, побайтно совпадает с `36bf1b2`. QA dataset digest `45c041165ad17f2f8114dddd454ba42f74e9e635eb44606133f291348626f413`, addendum SHA-256 `8c5cfda80ee90dea0e185d142249a03e6be83b7ec40f1523f07e74dcd5ed0b51`; привязки проверены, не мигрированы. **86 неизменяемых исторических файлов пакета** совпадают с `36bf1b2`, включая export и QA snapshots. Датированный [план С01.9](README.md) не является неизменяемым snapshot: до этого прохода он получил только документированную заметку comm_sound в С01.11. Полнота более ранней неизвестной браузерной истории остаётся UNKNOWN; текущий экспорт 10/10 проверен отдельно.

Существующие проверки — **57 tests PASS**:

```bash
python -m unittest tests.test_read_composition tests.test_composition_dictionary_baseline_v0_1 tests.test_composition_dictionary_final_qa_v0_2 tests.test_composition_dictionary_qa_migration_v0_2 tests.test_replica_package tests.test_dictionary_search_reasons -q
```

Две генерации в разных каталогах побайтно совпали с действующими артефактами. Reader: десять ID карточек, 0066, Corpus 0044/0022 — PASS; 0025 корректно возвращает CORPUS_ONLY без статьи. Реальный script viewer проверен в Node DOM fixture: поиск/фильтры/порядок/пояснения, отсутствие 0025, отдельная 0066. Браузер/deployment не проверялись; Renderer-check не является comprehension validation или новой авторской visual QA. `git diff --check` — PASS.

## Узкая сверка comm_sound — только этот primitive

- **Автор:** E `/records/2/creator_note`: «в целом коммуникация (разговор, сообщение, соц медия и тд - весь набор коммуникаций)»; «именно производимый (не звук дождя, животных и тд)»; «оральная, письменная и тд».
- **Dictionary:** D `/entries/5/usage_note`: `human communication (oral, written and social-media messages)`; `sound produced by people directly or through technical means: voice, rustling, playing music, a car.`; `Natural sounds such as rain and animal sounds are outside this definition.` Уточнение верно привязано к двум comm_sound-формам; глобальная LESS/DOWN синонимия не введена.
- **Lexicon:** [source](../../../../lexicon/icon-index.json) и [публичная копия](../../../lexicon/icon-index.json), `/icons/60/meaning_en`: `sound / audible signal / music / what is heard`. `/icons/60/aliases_en`: `sound`, `audio`, `audible signal`, `music`, `heard`. [Lexicon UI](../../../app.js) показывает meaning_en. FR/ES overlays не имеют отдельной comm_sound записи и используют fallback.
- **Composer:** [generated data](../../../composer/generated/pictiq-composer-data.mjs), `lexicon.icons[id=comm_sound]`, повторяет эти поля. [tokenLabel](../../../composer/composer-core.mjs) возвращает `sound / audible signal / music / what is heard` — подтверждено Node runtime. [app](../../../composer/app.mjs) использует его как palette-title и tooltip `sound / audible signal / music / what is heard · comm_sound`; palette-gloss — `sound, audio, audible signal`.

Расхождение: полная аудио-формулировка не охватывает письменную коммуникацию и не задаёт человеческий источник; `what is heard` шире авторского определения. Одна короткая метка Sound ошибку не доказывает. Runtime-поиск подтверждает: `communication` находит comm_sound, `written` и `social media` — нет. Минимально исправить **meaning_en / aliases_en** только comm_sound, согласовать публичную Lexicon-копию и пересоздать Composer data [существующим генератором](../../../../tools/generate_composer_data.py). Возможная meaning_en: `human communication / human-produced sound`; aliases должны обеспечивать поиск письменных сообщений/соцмедиа. Category/tags уже содержат communication. ID, SVG, схемы, остальные primitives и Dictionary Messages не требуют изменений; один description не исправит потребителей meaning_en/aliases_en.

## Оставшиеся вопросы и один следующий шаг

| Категория | Конкретная причина / evidence | Минимальный путь |
| --- | --- | --- |
| **BLOCKS DICTIONARY FREEZE** | **Нет фактического блокера фиксации исследовательского Dictionary:** все 10 решений согласованы, семь изменений применены, данные/история/генерация проверены. Внешние подписи не делают правильное Dictionary-описание 0006 неприменённым. | Отдельное явное решение о freeze; этот проход его не принимает. READY не означает FROZEN. |
| **BLOCKS PUBLIC RELEASE — PR1** | comm_sound в Lexicon/Composer имеет описанное выше неверное ограничение областью слышимого. Это влияет на выбор/прочтение знака в публичных инструментах, особенно для письменной коммуникации. | Только comm_sound meaning_en/aliases_en и их производные; без новых знаков/правил. |
| **BLOCKS PUBLIC RELEASE — PR2** | У текущей 0065, D `/entries/63/usage_note`, сохранено `This is distinct from a timetable/schedule request, which remains unresolved.` Это историческая фазовая заметка, не открытое семантическое решение: 0066 уже APPLIED. Reader даёт `RELATED_TIMETABLE_APPLIED`, но [viewer](../review/index.html) выводит usage_note обычным текущим текстом; реальный script подтвердил видимое `which remains unresolved`. | Пометить/пояснить эту фазовую заметку в публичном отображении по существующей A7, не переписывая источник и не меняя Messages. До этого не публиковать такое отображение как актуальное. Для research freeze это документированная статусная оговорка, а не неприменённое решение. |
| **NON-BLOCKING BACKLOG** | Старые PENDING/open/awaiting заголовки в датированных source/QA документах и текущий NOT FROZEN не означают, что предоставленный creator export снова UNREVIEWED. Новые примеры без ID, дополнительные композиции, Color Modifier, Translator/API и новые сценарии не входят в сверенную проекцию. | Историю сохранить; актуальные freeze-заголовки согласовывать только в отдельном разрешённом freeze-проходе. Не расширять текущий QA scope. |

**Один следующий проход:** исправить только meaning_en/aliases_en comm_sound и производные публичные данные (PR1); проверить подпись, tooltip и поиск. Без новой семантической QA и изменений Dictionary. PR2 — отдельный статусный вопрос отображения. Freeze, push, tag и release не выполнены.
